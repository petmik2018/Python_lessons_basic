# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def get_full_name(self):
        return self.name + " " + self.surname
        
class Student(Person):
    def __init__(self, name, surname, class_room, father, mother):
        Person.__init__(self,name, surname)
        self.class_room = class_room
        self.father = father
        self.mother = mother
    def get_class_room(self):
        return self.class_room
        
class Teacher(Person):
    def __init__(self, name, surname, science, class_list):
        Person.__init__(self,name, surname)
        self.science = science
        self.class_list = class_list
    def get_science(self):
        return self.science
    def get_class_list(self):
        return self.class_list
        
class Class_Description:
    def __init__(self, name, science_list, teacher_list):
        self.name = name
        self.science_list = science_list
        self.teacher_list = teacher_list
        
    def get_name(self):
        return self.name

students = [Student("Вася", "Иванов", "7А", "Иван Иванович", "Мария Ивановна"),
            Student("Миша", "Петров", "7А", "Василий Иванович", "Мария Петровна"),
            Student("Игорь", "Новиков", "7Б", "Аркадий Петрович", "Лариса Ивановна"),
            Student("Олег", "Тютюхин", "7Б", "Игорь Иванович", "Василиса Ивановна"),
            Student("Борис", "Борисов", "7В", "Борис Борисович", "Мария Борисовна"),
            Student("Никита", "Леонидов", "7В", "Алексей Иванович", "Елена Петровна")]
            
teachers = [Teacher("Иван Иванович","Иванов","математика", ["7А", "7Б"]),
            Teacher("Борис Моисеевич","Розенталь","математика", ["7В"]),
            Teacher("Алла Александровна","Александрова","литература", ["7А"]),
            Teacher("Ирина Иосифовна","Шпиц","литература", ["7Б", "7В"])]
            
classes = [Class_Description("7А", [], []),
            Class_Description("7Б", [], []),
            Class_Description("7В", [], [])]
            
def show_students_list():
    print("\nСПИСОК УЧЕНИКОВ В КЛАССАХ")
    for cl in classes:
        print("\nУченики класса ", cl.get_name())  
        for st in students:
            if st.get_class_room() == cl.get_name(): print(st.get_full_name()) 
            
def show_students_info():        
    print("\nИНФОРМАЦИЯ ОБ УЧЕНИКАХ")
    for st in students:
        my_class_room = st.get_class_room()
        print("\nУченик {} учится в классе {}".format(st.get_full_name(), my_class_room))
        for teach in teachers:
            if my_class_room in teach.get_class_list():
                science = teach.get_science()[:-1] + "у"
                print("Учитель {} преподает в этом классе {}".format(teach.get_full_name(), science))
                
def parents_info():            
    print("\nПОЛУЧЕНИЕ ИНФОРМАЦИИ О РОДИТЕЛЯХ")
    st_list = []
    for st in students:
        st_list.append(st.get_full_name())
    for i, st_name in enumerate(st_list):
        print(i, st_name)
    i = input("Выберите номер для информации: ")
    try:
        if int(i) in range(0, len(st_list)):
            print("Выбран ", st_list[int(i)])
            parents = list(filter(lambda x: x.get_full_name() == st_list[int(i)], students))
            print("Родители: отец {}, мать {}".format(parents[0].father, parents[0].mother))
            return 
        else:
            print("Направильно набран номер")
            return ""
    except ValueError:
        print("Вы что-то не то нажали")
        return ""
    
titles = {"1": "Список учеников в каждом классе",
        "2": "Информация обучениках и учителях",
        "3": "Информация о родителях учеников",}

actions_numbers = "123"

actions = {"1": show_students_list,
        "2": show_students_info,
        "3": parents_info}    
while True:
    print("\nВЫБЕРИТЕ ОПЕРАЦИЮ ИЗ СПИСКА:")
    for key in actions_numbers:
        print(key, titles[key])
    print("Q: Закончить работу с программой")
    key = input(" Ваш выбор: ")
    if key in actions_numbers:
        actions[key]()
    elif key == "Q":
        print("Давай, до свидания!")
        break
    else:
        print("Вы что-то не то нажали \n")
        