#!/usr/bin/python3

# Программа позволяет играть в лото в разных конфигурациях:
# Числа на карточках и бочонках берутся из диапазона от 1 до Num_max, возможно Num_max = 90
# Чтобы сыграть укороченную версию, уменьшите число Num_max, например, до 30
# Количество линий на карточках = Numbers_of_lines, для примера Numbers_of_lines = 3
# Количество позиций в линии  на карточках = Numbers_of_columns, для примера Numbers_of_columns = 9
# На каждой линии может располагаться Numbers_per_line чисел, для примера Numbers_per_line = 5

import random

def make_your_choice(title, char_1, char_2):
    # служебная функция для выбора из двух символов
    while True:
        choice = input(title)
        if choice == char_1 or choice == char_2:
            return choice
        else:
            print("Что-то не то нажали")

class IterObj:
    def __init__(self, iterations, num_max):
        self.i = 0
        self.iterations = iterations
        self.num_max = num_max
        self.numbers = []
        for i in range(0, self.num_max): self.numbers.append(i+1)

    def __next__(self):
        self.i += 1
        if self.i <= self.iterations:
            index = random.randint(1, len(self.numbers))
            num = self.numbers.pop(index-1)
            return num
        else:
            raise StopIteration

class Iter:
    # итератор генерирует последовательность НЕПОВТОРЯЮЩИХСЯ случайных чисел
    def __init__(self, iterations, num_max):
        self.iterations = iterations
        self.num_max = num_max
    def __iter__(self):
        return IterObj(self.iterations, self.num_max)
        
class Card:
    def __init__(self, title, num_max, number_of_lines, number_of_columns, numbers_per_line):
        self.title = title
        self.num_max = num_max
        self.number_of_lines = number_of_lines
        self.number_of_columns = number_of_columns
        self.numbers_per_line = numbers_per_line
        self.card = []
        # генерируется список из 15 случайных неповторяющихся чисел
        self.numbers = []
        obj = Iter(self.number_of_lines*self.numbers_per_line, self.num_max)
        for el in obj: self.numbers.append(el)
        # итератор в 5 чисел из 9 для расстановки чисел по линиям карточки
        obj = Iter(self.numbers_per_line, self.number_of_columns)

        for l in range(0, self.number_of_lines):
            # список из 15 случайных чисел нарезается на 3 списка по 5
            line_of_numbers = self.numbers[l*self.numbers_per_line:(l+1)*self.numbers_per_line]
            line_of_numbers.sort()
            # создается список из 5 случайных позиций 
            positions = []
            for el in obj: positions.append(el)
            positions.sort()
            # линия из 9 позиций заполняется 5-ю числами
            self.card.append([])
            j = 0
            for i in range(1, self.number_of_columns+1):
                if i in positions:
                    self.card[l].append(line_of_numbers[j])
                    j += 1
                else:
                    self.card[l].append("")
                    
    def __str__(self): 
#        print(self.numbers)
        result_string = ""
        for i in range(0, self.number_of_lines): 
            for el in self.card[i]:
                if el == "":
                    result_string += "  _"
                else:
                    result_string += str(el).rjust(3, " ")
            result_string += "\n"
        return "\n" + self.title + "\n" +result_string
        
    def has_this_number(self, num):
    # проверка на присутствие числа в карточке
        self.num = num
        if num in self.numbers:
            return True
        else:
            return False
            
    def remove(self, num):
    # удаление числа из карточки
        self.num = num
        self.numbers.remove(num)
        for i in range(0, self.number_of_lines): 
            if self.card[i].count(num):
                self.card[i][self.card[i].index(num)] = ""
                
    def game_over(self):
    # проверка карточки на пустоту
        return len(self.numbers) == 0

# параметры игры, для ускорения можно уменьшить Num_max,например, до 30
Num_max = 90
Numbers_of_lines = 3
Numbers_of_columns = 9
Numbers_per_line = 5

my_card = Card("ВАША КАРТОЧКА", Num_max, Numbers_of_lines, Numbers_of_columns, Numbers_per_line)
computer_card = Card("КАРТОЧКА КОМПЬЮТЕРА", Num_max, Numbers_of_lines, Numbers_of_columns, Numbers_per_line)
games = Iter(Num_max, Num_max)
round_rest = Num_max

for step in games: 
    print(my_card)
    print(computer_card)
    round_rest -= 1
    print("Очередной бочонок: {}, осталось раундов: {}".format(step,round_rest))
    
    # наверное, этот кусок можно написать покомпактней,
    # но через ветвления if-else хорошо видна логика, поэтому оставил так
    if computer_card.has_this_number(step):
            computer_card.remove(step)
            print("КОМПЬЮТЕР ВИДИТ У СЕБЯ ЧИСЛО {}".format(step))
    if make_your_choice("Сделайте Ваш выбор: зачеркнуть - Z, пропустить - C: ", "Z", "C") == "Z":
        if my_card.has_this_number(step):
            my_card.remove(step)
            print("БРАВО! ВЫ УСПЕШНО УБРАЛИ ЧИСЛО!!!")
        else:
            print("ОШИБКА! НЕТ ТАКОГО ЧИСЛА, ВАМ ЗАСЧИТАНО ПОРАЖЕНИЕ :((")
            break
    else:
        if my_card.has_this_number(step):
            print("ВЫ НЕВНИМАТЕЛЬНЫ, ПРОПУСТИЛИ ЧИСЛО {}".format(step))
            print("ВАМ ЗАСЧИТАНО ПОРАЖЕНИЕ :((")
            break
    if computer_card.game_over():
        print("К СОЖАЛЕНИЮ, ПОБЕДИЛ КОМПЬЮТЕР :((")
        break
    if my_card.game_over():
        print("ВЫ ПОБЕДИЛИ !!!!!")
        break
