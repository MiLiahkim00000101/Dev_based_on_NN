import kagglehub
from sklearn.feature_extraction.text import CountVectorizer
import os
import numpy as np
import shutil

def download_data():
    """
    Downloading of dataset from kaggle for solution(jensenbaxter/10dataset-text-document-classification)
    """
    # Download latest version
    os.makedirs("./data", mode=0o777, exist_ok=False)
    path = kagglehub.dataset_download("jensenbaxter/10dataset-text-document-classification")
    shutil.copytree(path, "data")


def documents_to_list(texts : list):
    """
    Make the list of all documents from dataset
    """
    dir_names = os.listdir("data/1")
    for dir in dir_names:
        filenames = os.listdir(os.path.abspath("data/1") + "/" + dir)
        for filename in filenames:
            with open((os.path.abspath("data/1") + "/" + dir + "/" + filename), "r") as file:
                texts.append(file.read())


def text_vectorizing(texts):
    """
    Creation of token matrix for all documents
    """
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    
    # Get feature names (vocabulary)
    feature_names = vectorizer.get_feature_names_out()
    print(f"Vocabulary size: {len(feature_names)} words")
    
    return X, vectorizer, feature_names


def Statistics(X):
    """
    Show result of vectorizing. Amount of elements in matrix, non-zero elements, zero elements, Sparse and Density of matrix
    """
    
    total_elements = X.shape[0] * X.shape[1]  # Всего элементов в матрице
    non_zero_elements = X.nnz                 # Ненулевых элементов
    zero_elements = total_elements - non_zero_elements # Нулевых элементов

    sparsity_ratio = zero_elements / total_elements
    density_ratio = non_zero_elements / total_elements


    print("Statistics: \n")
    print(f"Всего элементов в матрице: {total_elements}")
    print(f"Ненулевых элементов: {non_zero_elements}")
    print(f"Нулевых элементов: {zero_elements}")
    print(f"Разреженность (доля нулей): {sparsity_ratio:.2%}")
    print(f"Плотность (доля не нулей): {density_ratio:.2%}")


def print_vector_example(X, vectorizer, feature_names, text_index=1):
    """
    Print human-readable representation of one vector
    """
    print(f"\n=== Analysis of vector for document {text_index} ===")
    
    # Get the specific vector as a dense array
    vector_dense = X[text_index].toarray()[0]
    
    # Get non-zero elements and their values
    non_zero_indices = X[text_index].indices
    non_zero_values = X[text_index].data
    
    print(f"Vector shape: {X[text_index].shape}")
    print(f"Non-zero elements: {len(non_zero_values)}")
    print(f"Total elements: {X.shape[1]}")
    
    print("\nFirst 20 non-zero elements with word names:")
    for i, (idx, value) in enumerate(zip(non_zero_indices[:20], non_zero_values[:20])):
        word = feature_names[idx]
        print(f"  '{word}': {value}")
    
    if len(non_zero_values) > 20:
        print(f"  ... and {len(non_zero_values) - 20} more words")
    
    # Show some statistics about this vector
    print(f"\nVector statistics:")
    print(f"  Total words in document: {sum(non_zero_values)}")
    print(f"  Unique words in document: {len(non_zero_values)}")
    print(f"  Most frequent word: '{feature_names[non_zero_indices[np.argmax(non_zero_values)]]}' " 
          f"({max(non_zero_values)} occurrences)")

def main():
    # try:
    #     download_data()
    # except(FileExistsError):
    #     print("You already have folder \'data\' in your working directory. Please delete it to load dataset again.\n\n" \
    #     "If not, it's okay, programm will work correct with data you have previosly downloaded with given in readme link")

    print("\n\nExecution\n")

    texts = list() # This is the list of all documents in string format

    documents_to_list(texts)

    # Vectorize texts
    X, vectorizer, feature_names = text_vectorizing(texts)

    Statistics(X)

    # Print detailed analysis of one vector
    print_vector_example(X, vectorizer, feature_names, text_index=1)


if __name__ == '__main__':
    main()