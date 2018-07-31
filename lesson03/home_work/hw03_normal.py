# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    list_fibonacci = [1, 1] # числа Фибоначчи с номерами 0 и 1
    for i in range(1, m): # наращиваем список, имея в виду, что два элемента уже есть
        two_last_elements = list_fibonacci[-2:]
        list_fibonacci.append(sum(two_last_elements)) # в конец списка добавляется очередное число
    list_fibonacci = list_fibonacci[n:] # отрезаются первые n чисел
    return list_fibonacci

fibonacci(5, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    while True :
        changes = 0 # счетчик исправленных "беспорядков" в списке
        for i in range(0, len(origin_list)-1): # проходим по списку в поиске "беспорядков"
            if origin_list[i] > origin_list[i+1]: # "беспорядок" обнаружен
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i] # и устранен
                changes += 1
        if changes == 0: # если при очередном прохождении списка "беспорядков" не обнаружено, выходим из цикла
            break
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_function(a):
    return a > 0

def my_filter(filter_function,my_list):
    result = []
    for elem in my_list:
        if filter_function(elem):
            result.append(elem)
    return result

arr = [2, 0, -3, 7, -1, -10, 3]
print(my_filter(my_function, arr))
    
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1 = [0, 0]
A2 = [3, 0]
A3 = [3, 3]
A4 = [1, 3]

def difference(a, b):
    '''
     вектор определяется как разницы координат двух точех
    '''
    return [a[0]-b[0], a[1]-b[1]]

def parallel(a,b):
    '''
    если вектора параллельны, возвращается True
    '''
    return (a[0]*b[1]- a[1]*b[0] == 0)

vector1 = difference(A2, A1)
vector2 = difference(A3, A4)

# Проверяется условие попарной параллельности противоположных сторон

if parallel(difference(A1, A2), difference(A3, A4)) & parallel(difference(A2, A3), difference(A1, A4)):
    print("Это параллелограмм!!!")
else:
    print("Коряво получилось, на параллелорамм не похоже...") 