# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python hw05_hard.py param1 param2 param3
# После короткого обсуждения в телеге проблемы с "забыванием" смены директории
# завел файл config.txt для запоминания, откуда был последний выход
# по-хорошему, надо еще уметь выходить на уровень выше (cd..), но не успеваю

import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("ls - полное имя текущей папки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> <copy_name>- создание копии файла")
    print("rm <file_name> - удаление указанного файла")
    print("cd <path> - переход в выбранную директорию")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

# функция может принимать один или два параметра        
def file_copy():
    if not file_name:
        print("Необходимо указать хотя бы одно имя файла вторым параметром")
        return
    else:
        if target_name:
            new_name = target_name
        else:
            new_name = file_name + ".copy"
            print("Вы не указали имя файла-копии")
            print("поэтому по умолчанию")
        print("копируем в ", new_name) # это сообщение выводится в любом случае
    try:
        shutil.copy(file_name, new_name)
        print('файл {} скопирован'.format(file_name))
    except FileNotFoundError:
        print('файл {} не найден'.format(file_name))
        
def del_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        confirm = input("удалить файл {} ? Y/N ".format(file_name)) == "Y"
        if confirm:
            os.remove(file_name)
            print('файл {} успешно удален'.format(file_name))
    except FileNotFoundError:
        print('файл {} не найден'.format(file_name))
        
def show_dir():
    print(os.getcwd())

def ping():
    print("pong")
    
def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        config_file = open("config.txt", "w")
        config_file.write(dir_path) # при смене директории записываемся в config
        config_file.close()
        os.chdir(dir_path)
        print('вы перешли в новую директорию: {} '.format(dir_path))
    except FileNotFoundError:
        print('директория {} не существует'.format(dir_path))

# считываем имя последней активной директории и переходим в нее         
def read_config():
    try:
        config_file = open("config.txt", "r")
        new_dir = config_file.read()
        config_file.close()
        print(new_dir)
        os.chdir(new_dir)
        print('вы находитель в директории ', new_dir)
    except FileNotFoundError:
        print('файл  config не найден, вы остаетесь в корневой директории')

do = {
    "help": print_help,
    "ls" : show_dir,
    "mkdir": make_dir,
    "ping": ping,
    "cp" : file_copy,
    "rm" : del_file,
    "cd" : change_dir
}

read_config()

try:
    target_name = sys.argv[3] # имя файла, куда будем копировать
except IndexError:
    target_name = None
    
try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
except IndexError:
    dir_name = None
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

