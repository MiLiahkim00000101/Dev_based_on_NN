import numpy as np

def print_matrix_statistics(X):
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

    i = 0

    for i, (idx, value) in enumerate(sorted(zip(non_zero_indices, non_zero_values), key=lambda item: item[1], reverse=True)):
        word = feature_names[idx]
        print(f"  '{word}': {value}")
        if i == 20:
            break
    
    if len(non_zero_values) > 20:
        print(f"  ... and {len(non_zero_values) - 20} more words")
    
    # Show some statistics about this vector
    print(f"\nVector statistics:")
    # print(f"  Total words in document: {sum(non_zero_values)}") working only for CountVectorizer
    print(f"  Unique words in document: {len(non_zero_values)}")
    print(f"  Most important word: '{feature_names[non_zero_indices[np.argmax(non_zero_values)]]}'")