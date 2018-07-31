# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    mult = 10**ndigits
    number = number * mult
    number = round(number)
    return number/mult

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.4444451, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    numbers =[]
    for i in range(0,6):
        numbers.append(ticket_number % 10)
        ticket_number = ticket_number // 10
    return sum(numbers[:3]) == sum(numbers[3:])

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
