# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

def get_data_from_file(path, file_name):
#  Информация читается построчно из файла и заносится в список из строк
    path = os.path.join(path, file_name)
    file_data = open(path, "r", encoding='UTF-8')
    information = file_data.readlines()
    file_data.close()
    return information
    
class Worker:
    def __init__(self, name, surname, salary, profession, hours_norm):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.profession = profession
        self.hours_norm = hours_norm
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_salary_and_hours_norm(self):
        return [self.salary, self.hours_norm]
        
class Hours_of:
    def __init__(self, name, surname, hours):
        self.name = name
        self.surname = surname
        self.hours = hours
    def get_full_name(self):
        return self.name + " " + self.surname 
    def get_hours(self):
        return self.hours        
  
# из файлов считываются данные и загружаются в списки из экземпляров классов 
workers = []   
for line in get_data_from_file("data", "workers"):
    line = line.split(" ")         # строки нарезаются
    line = list(filter(len, line)) # и зачищаются от пустых символов
    if line[0] != "Имя":
        line[2] = int(line[2]) # преобразуем оклад в число
        line[4] = int(line[4].replace("\n","")) # и норматив часов тоже
        worker = Worker(line[0], line[1], line[2], line[3], line[4])
        workers.append(worker)
        
hours = []   
for line in get_data_from_file("data", "hours_of"):
    line = line.split(" ") # все аналогично со вторым файлом
    line = list(filter(len, line))
    if line[0] != "Имя":
        line[2] = int(line[2].replace("\n",""))
        hours_of_worker = Hours_of(line[0], line[1], line[2])
        hours.append(hours_of_worker)
        
for worker in workers:
    worker_name = worker.get_full_name()
    act_hours = list(filter(lambda x:x.get_full_name() == worker_name, hours))
    real_hours = act_hours[0].get_hours() # находится количество отработанных часов
    salary = worker.get_salary_and_hours_norm()[0] # находится основная зарплата
    hours_norm = worker.get_salary_and_hours_norm()[1] # находится норматив
        # вычисляется надбавка или вычет
    if real_hours > hours_norm:
        delta= salary/hours_norm * 2*(real_hours-hours_norm) # надбавка
    else:
        delta = salary/hours_norm *(real_hours-hours_norm) # вычет
    print("Гр. {} отработал {} часов". format(worker_name, real_hours))
    print("При зарплате {} и нормативе {}, получит {}".format(salary, hours_norm, salary+delta))

