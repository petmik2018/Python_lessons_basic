# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


# не подкачиваются свои библиотеки в Юпитере
# пришлось все делать в одном файле
# немного увлекся, зато вроде все работает

import os

# служебная функция для удобства работы с пунктами меню
# если неудобно, когда быстро прокручивается, убрать знак коммента
def press_any_key():
#    new_choice = input("Нажмите любую клавишу для продолжения")
    print("\n")
    return

# функция показывает имя текущей директории
def show_curr_dir():
    curr_dir = os.getcwd()
    print("Текущая папка: ", curr_dir)
    return

# функция выводит нумерованный список папок в текущей директории
# для последующего выбора пользователем по номеру
def show_dir_list():
    print("Список папок в текущей директории: ")
    curr_dir = os.getcwd()
    dir_list = os.listdir(curr_dir)
    dir_list = list(filter(lambda x: os.path.isdir(x), dir_list))
    for i, dir_name in enumerate(dir_list):
        print(i, dir_name)
        
# функция возвращает имя папки, выбранной пользователем из списка по номеру  
# если что-то не так (вместо номера что-то не то или номер некорректный),
# то возвращает ""      
def choose_dir(i):
    curr_dir = os.getcwd()
    dir_list = os.listdir(curr_dir)
    # Из содержимого текущей папки отфильтровываются только вложенные папки
    dir_list = list(filter(lambda x: os.path.isdir(x), dir_list))
    try:
        if int(i) in range(0, len(dir_list)):
            return dir_list[int(i)]
        else:
            print("Направильно набран номер")
            return ""
    except ValueError:
        return ""
    
# выбор и переход в выбранную папку
# выбор возможен только из существующих папок
# но проверку на существование на всякий случай оставил
def change_dir():
    show_dir_list()
    new_choice = input("Выбeрите нужную папку для перехода: ")
    new_dir = choose_dir(new_choice)
    print("Вы выбрали папку: ", new_dir)
    if new_dir:
        curr_dir = os.getcwd()
        dir_path = os.path.join(curr_dir, new_dir)
        try:
            os.chdir(dir_path)
            print("Переход в папку {} состоялся".format(new_dir))
        except FileNotFoundError:
            print("Папка {} не существует".format(new_dir))
    else:
        print("Переход в папку не состоялся")
    show_curr_dir()
    press_any_key()
    
# выводится содержимое текущей директории
def show_all():
    show_curr_dir()
    curr_dir = os.getcwd()
    dir_list = os.listdir(curr_dir)
    print("Содержимое текущей директории:")
    print(dir_list)
    press_any_key()

# выбор и удаление выбранной директории  
# выбор возможен только из существующих папок  
def del_dir():
    show_dir_list()
    new_choice = input("Выбeрите нужную папку для удаления: ")
    my_dir = choose_dir(new_choice)
    print("Вы выбрали папку: ", my_dir)
    if my_dir:
        curr_dir = os.getcwd()
        dir_path = os.path.join(curr_dir, my_dir)
        try:
            os.rmdir(dir_path)
            print("Папка {} удалена успешно".format(my_dir))
        except OSError:
            print("Папку {} не получается удалить".format(my_dir))
    else:
        print("Удаление не состоялось")
    press_any_key()

# создание новой папки, если таковой уже не существует
def create_dir():
    my_dir = input("Введите имя новой папки: ")
    if my_dir:
        curr_dir = os.getcwd()
        dir_path = os.path.join(curr_dir, my_dir)
        try:
            os.mkdir(dir_path)
            print("Папка {} успешно создана".format(my_dir))
        except FileExistsError:
            print("Папка {} уже существует".format(my_dir))
        return
    else:
        print("Создать папку не получилось")
    press_any_key()
    
    
titles = {"1": "Перейти в папку",
        "2": "Просмотреть содержимое текущей папки",
        "3": "Удалить папку",
        "4": "Создать папку"}

actions_numbers = "1234"

actions = {"1": change_dir,
        "2": show_all,
        "3": del_dir,
        "4": create_dir}

while True:
    print("ВЫБЕРИТЕ ОПЕРАЦИЮ ИЗ СПИСКА:")
    for key in actions_numbers:
        print(key, titles[key])
    print("Q: Закончить работу с программой")
    key = input(" Ваш выбор: ")
    if key in actions_numbers:
        actions[key]()
    elif key == "Q":
        print("Давай, до свидания!")
        break
    else:
        print("Вы что-то не то нажали \n")
        
