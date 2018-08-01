# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def ratio3(my_list):
    result = [0, 0, 1]
    '''
    Приведение введенной дроби (строки) к списку [ целая часть, числитель, знаменатель]
    Если дробной части нет, то [целая часть, 0, 1]
    '''
    my_list = my_list.split(" ")
    for elem in my_list:
        if elem: # ищем непустые элементы
            if "/" in elem : # это дробная часть, сплитим на числитель и знаменатель
                elem = elem.split("/")
                result[1] = int(elem[0])
                result[2] = int(elem[1])
            else:
                result[0] = int(elem)
    return result

def ratio2(list_3): # аргумент - список из 3-х элементов
    '''
    Приведение дроби с целой частью к неправильной (числитель/знаменатель), знак определяется числителем
    '''
    result = [0, list_3[2]]
    if list_3[0] < 0: # дробь отрицательная, если минус стоял перед целой частью
        result[0] = list_3[0]*list_3[2] - list_3[1] 
    else:
        result[0] = list_3[0]*list_3[2] + list_3[1]    # дробь положительная, если нет
    return result

def n_o_d(list_2):
    """
    Вычисление наибольшего общего делителя, причем list_2[0]<list[1] и положительны
    Алгоритм самый тупой, но, поскольку числа небольшие, для сдачи ДЗ сгодится
    """
    if list_2[1] % list_2[0] == 0:
        return list_2[0]
    else:
        for i in range(1, list_2[0])[::-1]:
            if list_2[0] % i == 0 and list_2[1] % i == 0:
                return i

def summa2(a ,b):
    '''
    Сложение неправильных дробей в виде списков из двух элементов
    '''
    result = []
    result.append(a[0]*b[1] + a[1]*b[0]) # числитель
    result.append(a[1]*b[1]) # знаменатель
    return result

def raznost2(a ,b):
    '''
    Вычитание неправильных дробей в виде списков из двух элементов
    '''
    result = []
    result.append(a[0]*b[1] - a[1]*b[0]) # числитель
    result.append(a[1]*b[1]) # знаменатель
    return result

def get_correct_ratio(list_2): #преобразование неправильной дроби к дроби с целой частью
    result = []
    if list_2[0] > 0:
        sign = 1
    else:
        sign = -1
        list_2[0] = (-1) * list_2[0]
    # преобразуем как положительную дробь
    result.append(sign*(list_2[0] // list_2[1])) # ставим знак на место
    result.append(list_2[0] % list_2[1])
    result.append(list_2[1])
    return result

# expression = input("Введите сумму дробей для вычисления:")
expression = "1    5/6 - 3/6" # предположим ввод в правильном порядке, через любое количество пробелов

print(expression)

if " + " in expression:
    my_array = expression.split(" + ")
    operation = "Сумма"
elif " - " in expression:
    my_array = expression.split(" - ")
    operation = "Разность"
else:
    print("В выражении не найден знак действия")

# вытаскиваем дроби из строки как списки из 3-х элементов:
# [целая часть, числитель дробной части, знаменатель дробной части]
a = ratio3(my_array[0])
b = ratio3(my_array[1])

# преобразуем в неправильные дроби, не забывая про знак (учтено в функции)
a = ratio2(a)
b = ratio2(b)

# вычисление в зависимости от типа операции
if operation == "Сумма":
    c = summa2(a, b)
else:
    c = raznost2(a, b)
    
# выделение целой части
c = get_correct_ratio(c)

# находим НОД числителя и знаменателя дробной части и сокращаем на него
a = n_o_d(c[-2:])
c[1] //= a
c[2] //= a
print("{} дробей равна {} {}/{}".format(operation, c[0], c[1], c[2]))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

def my_split(string_info):
    '''
    Строка преобразуется в список из непустых строк
    '''
    short_list = []
    a = string_info.split(" ")
    for elem in a:
        if elem != "":
            short_list.append(elem)
    short_list[1] += " " # имя и фамилия (первые два элемента) через пробел объединяются в один элемент
    short_list[1] += short_list[0]
    short_list.pop(0)
    return short_list
    
def list_in_line(my_list):
    '''
    Строится двумерный список из списка со строками
    '''
    new_list = []
    for element in my_list:
        new_list.append(my_split(element))
    return new_list
    
def get_data_from_list(worker, worker_list, data_number):
    '''
    В двумерном массиве worker_list ищется элемент, в котором worker стоит на первом месте
    и возвращается его под-элемент с места data_number
    '''
    for element in worker_list:
        if element[0] == worker:
            return element[data_number]

def get_list_from_file(path, file_name):
    '''
    Список читается построчно из файла и преобразуется в двумерный список
    '''
    path = os.path.join(path, file_name)
    file_data = open(path, "r", encoding='UTF-8')
    information = file_data.readlines()
    file_data.close()
    information = list_in_line(information)
    return information
    

# из файлов считываются данные и преобразуются в двумерные списки    
workers_info = get_list_from_file("data", "workers")
hours_info = get_list_from_file("data", "hours_of")

for worker in hours_info: # проходится список с отработанными часами
    worker_name = worker[0]
    if worker_name != "Фамилия Имя": # исключается первый элемент с заголовками столбцов
        real_hours = int(worker[1]) # находится количество отработанных часов
        salary = int(get_data_from_list(worker_name, workers_info, 1)) # находится основная зарплата
        hours_norm = int(get_data_from_list(worker_name, workers_info, 3)) # находится норматив
        # вычисляется надбавка или вычет
        if real_hours > hours_norm:
            delta= salary/hours_norm * 2*(real_hours-hours_norm) # надбавка
        else:
            delta = salary/hours_norm *(real_hours-hours_norm) # вычет
        print("Гр. {} отработал {} часов". format(worker_name, real_hours))
        print("При зарплате {} и нормативе {}, получит {}".format(salary, hours_norm, salary+delta))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os
import shutil

def get_list_from_file(path, file_name):
    ''' 
    Данные из файоа считываются в список
    '''
    path = os.path.join(path, file_name)
    file_data = open(path, 'r', encoding='UTF-8')
    information = file_data.readlines()
    file_data.close()
    return information
    
def write_fruit_to_file(letter):
    '''
    Данные записываются в файл согласно параметру letter 
    '''
    path_res = os.path.join("res", "fruit_" + first_letter + ".txt")
    file_fruits = open(path_res, letter, encoding='UTF-8')
    file_fruits.write(fruit_name)
    file_fruits.close()
    return 0
    
fruits_list = get_list_from_file("data", "fruits.txt")
letter_list = [] # создается список первых букв

if "res" in os.listdir():
    shutil.rmtree("res") # удаление папки со старыми результатами, если она есть в текущей папке

os.mkdir("res") # создание новой пустой папки для записи результата
for fruit_name in fruits_list:
    first_letter = fruit_name[0]
    if first_letter in list(map(chr, range(ord('А'), ord('Я')+1))): # обходим служебные символы
        if letter_list.count(first_letter) == 0: # если буквы в списке нет, добавляем, и открываем файл с нуля
            letter_list.append(first_letter)
            write_fruit_to_file("x")
        else:
            write_fruit_to_file("a") # если буква в списке есть, то открываем файл для дозаписи

