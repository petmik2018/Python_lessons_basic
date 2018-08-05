# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

       # -----------первый способ----------
import re
result = re.split(r"[ABCDEFGHIJKLMNOPQRSTUVWXYZ]+", line)
print(result)


#----------второй способ----------------
new_line = ""
symbols_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for sym in line:
    if sym in symbols_upper:
        new_line += " "
    else:
        new_line += sym
new_line = list(filter(len, new_line.split(" ")))
print(new_line)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
       
#------------------первый способ-------------
import re
# line_2 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"

pattern = '[a-z][a-z] *[A-Z]*[A-Z][A-Z]'

my_line= re.findall(pattern, line_2)
result = list(filter(None,[elem[2:][:-2] for elem in my_line]))

print("Решение с использованием re")
print(result)


#---------------второй способ-----------------
# дает другой ответ, но формально соответствующий условию задачи
# в строке "ABCD" 2 символа в верхнем регистре стоят справа у "A" и "B"
# line_2 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"

symbols_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols_lower = "abcdefghijklmnopqrstuvwxyz"

i = 0
to_find = False
result = []

# ищем строку с двумя символами Lower в начала и с двумя символами upper в конце
while i < len(line_2)-2: # ищем предполагаемое начало строки из 2-х символов lower
    two_sym_start = line_2[i] + line_2[i+1]
    if two_sym_start.islower():
        to_find = True
    i += 1
    j = i + 1
    while j < len(line_2)-2: # ищем возможное окончание строки из 2-х символов uppre
        two_sym_end = line_2[j] + line_2[j+1]
        if two_sym_end.isupper():
            if to_find:
    # проверяем середину, чтобы все символы были upper
                if line_2[i+1:j].isupper(): result.append(line_2[i+1:j])
        j += 1
    to_find = False
    
print("Решение без использования re")
print(result)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random
import re

Num_number =  2500 # количество знаков длинного числа

# функция возвращает максимальную длину включения цепочки одинаковых символов в строке
def max_length(line, sym):
    i = 0
    num_find = 0
    while num_find > -1:
        i += 1
        num_find = line.find(sym*i)
    return i-1

# открывается файл с именем long_number.txt
path = os.path.join("res", "long_number.txt")
my_file = open(path, "w")

# в файл записывается число из Num_number случайных цифр

for _ in range(0, Num_number):
    num = random.randint(0,9)
    my_file.write(str(num))
my_file.close

# длинное число считывается из файла
my_file = open(path, "r")
for line in my_file: line
my_file.close
# можно для контроля вывести число целиком
# print(line)

# формируется список максимальных длин цепочек повторяющихся цифр от 0 до 9
len_list = [max_length(line, str(i)) for i in range(0,10)]
# выаодится максимальная из всех
for i in range(0, 10):
    if len_list[i] == max(len_list):
        print("Максимальное количество цифр подряд:", str(i)*len_list[i])

