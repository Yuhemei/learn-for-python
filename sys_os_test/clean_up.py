import os
import sys


def clean_up(dir_path):
    file_list = os.listdir(dir_path)
    for item in file_list:
        file_name, file_suffix = os.path.splitext(item)
        if file_name == 'clean_up':
            continue
        print(file_name)
        dir_name = file_suffix.split('.')[1]
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        os.rename(item, dir_name + '/' + item)
    print("success")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception('please set the dir')
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        raise Exception("please input a dir name")
    clean_up(dir_path)