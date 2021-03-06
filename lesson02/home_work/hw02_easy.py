# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0
lenMax = 0
# нахождение максимальной длины элементов списка
for fruit in fruits:
	if len(fruit) > lenMax:
		lenMax = len(fruit)

# формирование строки вывода с выравниваем по правой границе
# в зависимости от максимальной длины элемента
lenMax = str(lenMax)
print(lenMax)
printString = "{}.{:>" + lenMax + "}"
print(printString)

# вывод
for fruit in fruits:
	i += 1
	print(printString.format(i, fruit))
	

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

listMain = [1, 2, 4, 5, 6, 2, 4, 5, 1, 2, 6]
listEx = [1, 4]

for element in listMain: # перебор всех элементов в первом списке
	if element in listEx:  # проверяем есть ли текущий элемента во втором списке
		listMain.remove(element)
print(listMain)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

listMain = [1, 2, 4, 5, 6, 2, 4, 5, 1, 2, 6]
listTarget = []

# тут все просто читается по коду

for element in listMain:
	if element % 2 == 0:
		listTarget.append(element/4)
	else:
		listTarget.append(element*2)
		
print("Исходник:", listMain)		
print("Результат:", listTarget)