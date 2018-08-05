# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a = [1, 2, 4, 0]
b = list(elem**2 for elem in a)
print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ["яблоко", "груша", "тыква", "огурец"]
list2 = ["тыква", "яблоко"]

list3 = [fruit for fruit in list1 if list2.count(fruit)]
print(list3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

n = 100

list_of_numbers = [random.randint(-100, 100) for _ in range(0, n)]
# print(list_of_numbers)
my_list = list(elem for elem in list_of_numbers if elem%3 == 0 and elem>0 and elem%4)

print(my_list)