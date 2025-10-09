import kagglehub
import shutil

def download_data(type_of_path, dir_name):
    """
    Downloading of dataset from kaggle for solution(jensenbaxter/10dataset-text-document-classification)
    """
    # Download latest version
    path = kagglehub.dataset_download("jensenbaxter/10dataset-text-document-classification")
    if type_of_path == 'r':
        shutil.copytree(path, "./" + dir_name, dirs_exist_ok=True)
    else:
        shutil.copytree(path, dir_name, dirs_exist_ok=True)
   