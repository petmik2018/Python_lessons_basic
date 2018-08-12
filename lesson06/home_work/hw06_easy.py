# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math
# для определения треугольника надо обозвать вершины буквами
# и задать координаты вершин парами
class Triangle:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c 
      
    def length(self, x, y):# вспомогательная функция для вычисления расстояния между точками
        return math.sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))
    
    def get_perimeter(self):
        return self.length(self.a, self.b) + self.length(self.b, self.c) + self.length(self.c, self.a)

    def get_square(self): # площадь = половина векторного произведения любых двух строн
        s = ((self.b[0]-self.a[0])*(self.c[1]-self.a[1]) - (self.b[1]-self.a[1])*(self.c[0]-self.a[0]))/2
        return abs(s)# на случай, если треугольник не в ту сторону закручен (пригодится для трапеции) 
    
    def get_h(self, char_top):
        ind = self.name.find(char_top)
        if ind == -1:
            return "Нет такой вершины: " + char_top
        else:
            list_tops = []
            list_tops.append(self.a)
            list_tops.append(self.b)
            list_tops.append(self.c) 
            x = list_tops[(ind + 1) % 3]
            y = list_tops[(ind + 2) % 3]
            l = self.length(x, y)
            s = self.get_square()
            h = 2*s / l
            return "Высота из вершины {} равна: {}".format(char_top, h)
            
# для определения треугольника надо обозвать вершины буквами
# и задать координаты вершин парами
abc = Triangle("abc", [0,0], [2,0], [0,2])

print("Площадь треугольника: ", abc.get_square())
print("Периметр треугольника: ", abc.get_perimeter())
print(abc.get_h("b"))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
# для определения трапеции (и вообще любого 4-угольника)
# надо обозвать вершины буквами и задать координаты вершин парами
class Trapetion:
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a 
        self.b = b 
        self.c = c 
        self.d = d 
        
    def length(self, x, y):# вспомогательная функция для вычисления расстояния между точками
        return math.sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))  
    
    def get_triangle_square(self, x, y, z):# вспомогательная функция для вычисления площади треугольника
        s = ((y[0]-x[0])*(z[1]-x[1]) - (y[1]-x[1])*(z[0]-x[0]))/2
        return abs(s)# на случай, если треугольник не в ту сторону закручен (пригодится для трапеции) 
        
    # проверка является ли 4-угольник трапецией и если да, то равнобокой или нет   
    def self_test(self):
        if (self.b[0]-self.a[0]) * (self.c[1]-self.d[1]) == (self.b[1]-self.a[1]) * (self.c[0]-self.d[0]):
            if self.length(self.b, self.c) == self.length(self.a, self.d):
                return "Трапеция с основаниями ab и сd, равнобочная"
            else:
                return "Трапеция с основаниями ab и сd, неравнобочная"
        elif (self.c[0]-self.b[0]) * (self.d[1]-self.a[1]) == (self.c[1]-self.b[1]) * (self.d[0]-self.a[0]):
            if self.length(self.a, self.b) == self.length(self.c, self.d):
                return "Трапеция с основаниями bc и ad, равнобочная"
            else:
                return "Трапеция с основаниями bc и ad, неравнобочная"
        else:
            return("Это не трапеция!!!")
            
    def side_length(self, char_1, char_2):# для задания стороны нужно ввести имена углов
        if char_1 in self.name and char_2 in self.name:
            dict_tops = {self.name[0]:self.a, self.name[1]:self.b,
                            self.name[2]:self.c, self.name[3]:self.d}
            return "Длина стороны {}{} равна: {}". format(char_1, char_2, self.length(dict_tops[char_1], dict_tops[char_2]))
        else:
            return "Таких вершин не найдено"
            
    def get_perimeter(self):
        perim = self.length(self.a, self.b)
        perim += self.length(self.b, self.c)
        perim += self.length(self.c, self.d)
        perim += self.length(self.d, self.a)
        return perim
        
    def get_square(self):
        return self.get_triangle_square(self.a, self.b, self.c) + self.get_triangle_square(self.a, self.c, self.d)
        
# для определения трапеции (и вообще любого 4-угольника)
# надо обозвать вершины буквами и задать координаты вершин парами
        
abcd = Trapetion("abcd", [0,0], [5,0], [4,3], [1,3])
print(abcd.self_test())
print(abcd.side_length("c", "d"))
print("Периметр 4-угольника равен: ", abcd.get_perimeter())
print("Площадь 4-угольника равна: ", abcd.get_square())
