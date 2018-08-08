# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Скрипт, создающий папки

import os

def mk_dir_list():
    curr_dir = os.getcwd()
    print("Текущая папка: ", curr_dir)
    for i in range(1, 10):
        new_dir_name = "dir_" + str(i)
        dir_path = os.path.join(curr_dir, new_dir_name)
        try:
            os.mkdir(dir_path)
            print("Папка {} создана успешно".format(new_dir_name))
        except FileExistsError:
            print("Папка {} уже существует".format(new_dir_name))
            
def del_dir_list():
    curr_dir = os.getcwd()
    print("Текущая папка: ", curr_dir)
    for i in range(1, 10):
        new_dir_name = "dir_" + str(i)
        dir_path = os.path.join(curr_dir, new_dir_name)
        try:
            os.rmdir(dir_path)
            print("Папка {} удалена успешно".format(new_dir_name))
        except FileNotFoundError:
            print("Папка {} не существует".format(new_dir_name))
 
mk_dir_list()

# скрипт, удаляющий папки

import os

def del_dir_list():
    curr_dir = os.getcwd()
    print("Текущая папка: ", curr_dir)
    for i in range(1, 10):
        new_dir_name = "dir_" + str(i)
        dir_path = os.path.join(curr_dir, new_dir_name)
        try:
            os.rmdir(dir_path)
            print("Папка {} удалена успешно".format(new_dir_name))
        except FileNotFoundError:
            print("Папка {} не существует".format(new_dir_name))

del_dir_list()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def show_dir_list():
    curr_dir = os.getcwd()
    print("Текущая папка: ", curr_dir)
    dir_list = os.listdir(curr_dir)
    dir_list = list(filter(lambda x: os.path.isdir(x), dir_list))
    print("Список папок текущей директории:")
    for i, dir_name in enumerate(dir_list):
        print(i, dir_name)
    
show_dir_list()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil

curr_file_name = sys.argv[0]
new_file_name = curr_file_name + ".copy"
shutil.copy(curr_file_name, new_file_name)
