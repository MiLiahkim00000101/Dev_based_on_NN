import os

def documents_to_list(abs_rel_path : str, dir_name : str, texts : list):
    """
    Make the list of all documents from dataset
    """
    if abs_rel_path == 'a':
        dir_names = os.listdir(dir_name)
    else:
        dir_names = os.listdir(dir_name)
    for dir in dir_names:
        filenames = os.listdir(os.path.abspath(dir_name) + "/" + dir)
        for filename in filenames:
            try:
                with open((os.path.abspath(dir_name) + "/" + dir + "/" + filename), "r") as file:
                    texts.append(file.read())
            except Exception as e:
                raise IOError(f"Ошибка прочтения файла: {e}")
