# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

list1 = [2, -5, 8, 9, -25, 25, 4] 
result = []

for number in list1:
	if number>= 0.0: # извлекаем конень только из неотрицательных чисел
		sqrtCurr = math.sqrt(number)
		if int(sqrtCurr)==sqrtCurr: # имеет ли корень десятичную часть?
			result.append(int(sqrtCurr))
print(result)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

myDate = "02.11.2013"

day = myDate[0:2]
month = myDate[3:5]
year = myDate[6:10]

# формирование вспомогательного списка от 1 до 31 из 2-х символов; '01', '02',  и т.д.
num = []
for i in range(1,32):
	if i<10:
		num.append("0" + str(i))
	else:
		num.append(str(i))

# вспомогательный список для формирования числительных		
numWord1 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

# начало формирования списка числительных
daysList = ["Первое", "Второе", "Третье", "Четвертое", "Пятое", "Шестое", "Седьмое", "Восьмое",
		"Девятое", "Десятое", "Одиннадцатое", "Двенадцатое", "Тринадцатое", "Четырнадцатое"]

# список месяцев, наверное, есть встроенный, но я не нашел		
monthesList = ["января", "февраля", "марта", "апреля", "мая", "июня",
			"июля", "августа", "сентября", "октября", "ноября", "декабря"]
			
# дополнение списка числительных для 15-19
for i in range(4,9):
	newStr = str(numWord1[i][:-1])+"надцатое"
	daysList.append(newStr.title())
	
# это понятно
daysList.append("Двадцатое")

# дополнение списка числительных для 21-29
for i in range(0,9):
	newStr = "Двадцать " + daysList[i].lower()
	daysList.append(newStr)
	
# это понятно

daysList.append("Тридцатое")
daysList.append("Тридцать первое")

# формирование словарей дат и месяцев
daysDict = {num[i]:daysList[i] for i in range(0,31)}
monthesDict = {num[i]:monthesList[i] for i in range(0,12)}

# вывод искомого 
print("Дата {} в текстовом виде: {} {} {} года". format(myDate, daysDict[day], monthesDict[month], year))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

myList = []
n = input("Введите желаемое количество чисел: ")

for i in range(0,int(n)):
	randomNumber = random.randint(-100,100)
	myList.append(randomNumber)
print(myList)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

listStart = [1, 2, 4, 5, 6, 2, 5, 2]
listTarget1 = []
listTarget2 = []
print("Исходник:",listStart)

# ------------пункт а----------------
for element in listStart: # Перебор всех элементов из первого списка
	if element in listTarget1: # Проверяем есть ли текущий элемент в динамическом второго списка
		pass
	else:                      # если его там нет, добавляем
		listTarget1.append(element)
		
print("Список без повторов:",listTarget1)

# ------------пункт б----------------		
for element in listStart: # Перебор всех элементов из первого списка
	if listStart.count(element) == 1: # если элемент присутствует один раз, добавляем во второй список
		listTarget2.append(element)	
		
print("Элементы без повторений:",listTarget2)