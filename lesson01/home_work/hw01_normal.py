
__author__ = 'Петухов Михаил Юрьевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# версия с использованием цикла while
x = 58375
numberCurrent = 0
numberMax = 0

while x != 0 :
	numberCurrent = x % 10
	if numberCurrent > numberMax :
		numberMax = numberCurrent
	x = x // 10
print("Maximal number: ", numberMax)

# версия с использованием цикла for
x = 45683
numberMax = '0'

for numberCurrent in str(x) :
	print(numberCurrent)
	if numberCurrent > numberMax :
		numberMax = numberCurrent
print("Maximal number: ", numberMax)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# версия через действия над числами

a = input("Input first value, please: ")
b = input("Input first value, please: ")
print("First value : ", a, "; Second value : ", b)
a = int(a)
b = int(b)
a = a + b
b = a - b
a = a - b 
print("Change is completed!")
print("First value : ", a, "; Second value : ", b)


# версия с использованием синтаксиса кортежей (нагуглил)

a = input("Input first value, please: ")
b = input("Input first value, please: ")
print("First value : ", a, "; Second value : ", b)
a, b = b, a
print("Change is completed!")
print("First value : ", a, "; Second value : ", b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

while True : # ввод первого коэффициента с проверкой на 0
	a = input("Input 1st coefficient : ")
	if a == "0" :
		print("The 1st coefficient must be not zero! Please, try again.")
	else:
		break
b = input("Input 2nd coefficient : ") # ввод второго коэффициента
c = input("Input 3rd coefficient : ")  # ввод третьего коэффициента
print("To solve : ", a, "*x*x + ", b, "*x + ", c, " = 0" )

# преобразование коэффициентов в числовые переменные
a = float(a) 
b = float(b)
c = float(c)

discriminant = b*b - 4*a*c # вычисление и печать дискриминанта
print("Discriminant = ", discriminant)

if discriminant<0 :
	print("No roots :((")
elif discriminant == 0:
	print("One root only : ", -b/2/a)
else :
	print("Two roots : ", (-b + math.sqrt(discriminant))/2/a, " ; ", (-b - math.sqrt(discriminant))/2/a)
	