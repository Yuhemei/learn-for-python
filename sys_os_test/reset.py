import os
import sys


def reset(dir_path):
    #
    dir_list = os.listdir(dir_path)
    for item in dir_list:
        print("item:", item)
        item_path = dir_path + '/' + item
        if os.path.isdir(item_path):
            reset(item_path)
        elif os.path.isfile(item_path):
            print("item_path:", item_path)
            os.rename(item_path, dir_path + item)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception('please set the dir')
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        raise Exception("please input a dir name")
    reset(dir_path)