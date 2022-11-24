import csv
import os


def create_csv1(name_class_good: str, name_class_bad: str, name_annatation: str) -> None:
    '''The function of creating a csv file with 3 parameters: absolute path, relative path, class name'''
    with open(name_annatation, mode="w", encoding="UTF-16", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        name_good = os.path.join("dataset", name_class_good)
        name_bad = os.path.join("dataset", name_class_bad)
        list_good = os.listdir(name_good)
        list_bad = os.listdir(name_bad)
        for elem in list_good:
            abspath_good = os.path.join(os.path.abspath(name_class_good), elem)
            name_good_otnos = os.path.join(name_good, elem)
            writer.writerow([abspath_good, name_good_otnos, name_class_good])
        for elem in list_bad:
            abspath_bad = os.path.join(os.path.abspath(name_class_bad), elem)
            name_bad_otnos = os.path.join(name_bad, elem)
            writer.writerow([abspath_bad, name_bad_otnos, name_class_bad])
    pass

