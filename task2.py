import csv
import os
import shutil


def create_dir(dir_name: str) -> None:
    '''The function of creating a new directory with the specified name dir_name'''
    name_dir_folder = os.path.join(dir_name, "dataset")
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    if not os.path.isdir(name_dir_folder):
        name = os.path.join(dir_name, "dataset")
        os.mkdir(name)

def copy_dir2(good_name: str, bad_name: str, dir_name: str, annotation_name: str) -> None:
    '''
    the function copies the dataset to a 
    new directory with changes in the file name (number.txt->classname_number.txt) by means of creating 
    this directory using the dir_create function and writes the absolute path, 
    relative path and class name to a new csv file to be able 
    to define the instance class
    '''
    create_dir(dir_name)
    good = os.path.join("dataset", good_name)
    bad = os.path.join("dataset", bad_name)
    list_good = os.listdir(good)
    list_bad = os.listdir(bad)
    for file_dataset in os.listdir("dataset"):
        path_p = os.path.join("dataset", file_dataset)
        class_name = os.listdir(path_p)
        for elem in class_name:
            old_file = os.path.join(path_p, elem)
            new_file = os.path.join(
                dir_name, "dataset", f"{file_dataset}_{elem}")
            shutil.copy(old_file, new_file)
            with open(os.path.join(dir_name, annotation_name), mode="a", encoding="UTF-16", newline='') as f:
                writer = csv.writer(f, delimiter=';')
                abspath_f = os.path.join(os.path.abspath(
                    dir_name), f"{file_dataset}_{elem}")
                otnos_path = os.path.join(dir_name, f"{file_dataset}_{elem}")
                writer.writerow([abspath_f, otnos_path, file_dataset])
            pass