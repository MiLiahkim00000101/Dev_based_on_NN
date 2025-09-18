import kagglehub
from sklearn.feature_extraction.text import CountVectorizer
import os
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

    return X


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




def main():
    try:
        download_data()
    except(FileExistsError):
        print("You already have folder \'data\' in your working directory. Please delete it to load dataset again.\n\n" \
        "If not, it's okay, programm will work correct with data you have previosly downloaded with given in readme link")

    print("\n\nExecution\n")

    texts = list() # This is the list of all documents in string format

    documents_to_list(texts)

    X = text_vectorizing(texts) 

    Statistics(X)


if __name__ == '__main__':
    main()