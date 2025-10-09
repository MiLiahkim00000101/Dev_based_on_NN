import argparse

# import Data_download.downl as downl

from Data_download import downl
from Form_corpus import form_corpus 
from Vectorize_data import vectorize_data as vd
from Stat_out import show_stat as sh_s



def main():
    parser = argparse.ArgumentParser(description='Process directory to save data')
    parser.add_argument('--type_path', type=str, nargs=1, default='r',
                        help='using of absolute or relative path type \'a\' to use absolute and \'r\' to use relative,\n \'r\' is default')
    parser.add_argument('data_dir_name', type=str, nargs=1,
                        help='name of directory which will be using to save data')

    args = parser.parse_args()

    if args.type_path[0] != 'a' and args.type_path[0] != 'r':
        print("Please enter correct type of path. Use --help to see options.")
        return
    
    # Загружаем данные
    downl.download_data(args.type_path[0], args.data_dir_name[0])


    # Переведем каждый документ в элемент списка texts
    texts = list() 

    form_corpus.documents_to_list(args.type_path[0], args.data_dir_name[0], texts)

    print("==============Черёд статистики CountVectorizer:==============")
    # Векторизация с использованием count_Vectorizer
    X_countV, vectorizer, feature_names = vd.text_vectorizing(texts, "CountVec")

    sh_s.print_matrix_statistics(X_countV)

    sh_s.print_vector_example(X_countV, vectorizer, feature_names, text_index=1)

    # Векторизация с использованием TF-IDF
    print("\n\n==============Черёд статистики TF-IDF:==============")
    X_tfidf, vectorizer, feature_names = vd.text_vectorizing(texts, "TF-IDF")

    sh_s.print_matrix_statistics(X_tfidf)

    sh_s.print_vector_example(X_tfidf, vectorizer, feature_names, text_index=1)


if __name__ == "__main__":
    main()