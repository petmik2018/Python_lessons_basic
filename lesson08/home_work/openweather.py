# В силу недостатка времени и знаний предоставляю законченную версию программы,
# выдающую информацию о текущей погоде в любом городе мира
# Для получения информации необходимо сначала выбрать страну
# Для облегчения выбора страны предлагается ввести несколько первых букв названия
# Например, "R" или "Ru" или "Rus" и т.п.
# Для облегчения выбора города из выбранной страны
# предлагается ввести несколько первых букв названия
# Например, "B" или "Bo" или "Bos" и т.п.
# Для Москвы работает, для Бостона тоже. На Париже почему-то заткнулась, что-то не то с данными о направлении ветра

# -*- coding: utf-8 -*-       
import json
import codecs
import re
import urllib.request
import gzip
import os

class Country:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class City:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.country = data["country"]
        self.coord = data["coord"]
        
def get_num_elements_with_chars(data_list, chars = ""):
    l = len(chars)
    new_list = list(filter(lambda x: x.name[:l] == chars, data_list))
    return len(new_list)
        
def get_list_filtered_by_name(data_list, chars = ""):
    l = len(chars)
    if l :
        new_list = list(filter(lambda x: x.name[:l] == chars, data_list))
        if new_list == []: print("Ничего не найдено, повторите выбор")
        return new_list
    else: return data_list
    
def get_list_filtered_by_id(data_list, my_id):
    new_list = list(filter(lambda x: x.country == my_id, data_list))
    if new_list == []: print("Ничего не найдено, повторите выбор")
    return new_list

    
def get_list_element_id_name(data_list):
    i = 0
    print("\n")
    for el in data_list:
        i += 1
        print(i, el.id, el.name)
    while True:
        index = input("Выберите номер: ")
        try:
            index = int(index)
            if index in range(1, len(data_list)+1):
                print("Ваш выбор: ", data_list[index-1].name)
                return [data_list[index-1].id, data_list[index-1].name]
            else: print("Нет такого номера в списке")
        except ValueError:
            print("Вы что-то не так выбрали")
             
def get_list_from_json_file(path):
    fileObj = codecs.open( path, "r", "utf_8_sig" )
    text = fileObj.read()
    return json.loads(text)
    
def choose_country():
    print("Загружается список стран...")
    response = urllib.request.urlopen("http://country.io/names.json")
    res_file = open("countries.txt", "w", encoding = "UTF-8")
    res_file.write(str(response.read()))
    res_file.close()
    print("Список стран загружен")
     
    data_file = open("countries.txt")
    data_string = data_file.read()
    list_codes = re.findall(r"[A-Z]{2}", data_string)
    data_string = re.sub(r"[A-Z]{2}", "...", data_string)
    list_countries = re.findall(r"[a-zA-Z\s,-]{4,}", data_string)

    countries = []
    for i in range(0, len(list_codes)):
        new_country = Country(list_codes[i], list_countries[i])
        countries.append(new_country)

    chars = ""
    c_list = countries
    while True:
        print("\nВ списке стран {} позиций".format(get_num_elements_with_chars(c_list, chars)))
        print("\nВОЗМОЖНЫЕ ДЕЙСТВИЯ")
        print("1: Сократить список вводом нескольких первых букв")
        print("2: Выбрать позицию из списка")
        print("Q: Завершить работу")
        index = input("Ваш выбор: ")
        if index == "Q":
            break
        elif index == "1":
            chars = input("Dведите несколько первых букв названия, начиная с заглавной: ")
            c_list = get_list_filtered_by_name(countries, chars)
        elif index == "2":    
            my_country_info = get_list_element_id_name(c_list)
            return my_country_info
            if my_country: break
        else:
            print("Неправильный выбор")
 
def choose_city(country): 
    print("Загружается список городов из страны: ", country)
    response = urllib.request.urlopen("http://bulk.openweathermap.org/sample/city.list.json.gz").read()
    res_file = open("arch.gz", "wb")
    res_file.write(response)
    res_file.close()
    print("Список городов загружен...")
    inF = gzip.open("arch.gz")
    res_file = open("cities.json", "wb")
    s = inF.read()
    res_file.write(s)
    res_file.close()
    inF.close()
    print("и распакован")

    path = "cities.json"
    data_city = get_list_from_json_file(path)
       
    city_list = []
    for city_info in data_city:
        new_city = City(city_info)
        city_list.append(new_city)
        
    cities = get_list_filtered_by_id(city_list, country)
    chars = ""
    c_list = cities
    while True:
        print("\nВ списке городов {} позиций".format(get_num_elements_with_chars(c_list, chars)))
        print("\nВОЗМОЖНЫЕ ДЕЙСТВИЯ")
        print("1: Сократить список вводом нескольких первых букв")
        print("2: Выбрать позицию из списка")
        print("Q: Завершить работу")
        index = input("Ваш выбор: ")
        if index == "Q":
            break
        elif index == "1":
            chars = input("Dведите несколько первых букв названия, начиная с заглавной: ")
            c_list = get_list_filtered_by_name(cities, chars)
        elif index == "2":    
            my_city_info = get_list_element_id_name(c_list)
            return my_city_info
            if my_city: break
        else:
            print("Неправильный выбор")
            
def get_weather_info(city, country):
    city_url = "http://api.openweathermap.org/data/2.5/weather?id={}&appid=b502f7497af3a5db6ecd6460ccdd9e01".format(city[0])
    response = urllib.request.urlopen(city_url)
    res_file = open("result.txt", "w", encoding = "UTF-8")
    res_file.write(str(response.read()))
    res_file.close()
    # на всякий случай записали информацию в файл и теперь читаем из него 
    path = "result.txt"
    fileObj = codecs.open( path, "r", "utf_8_sig" )
    text = fileObj.read()
    info = text.replace("b'","[")
    info = info[:-1] +"]"
    info = json.loads(info)
    info = info[0]
        
    print("\nИНФОРМАЦИЯ О ПОГОДЕ  В ГОРОДЕ:", city[1], ", ", country[1])
    print("Состояние неба: ",info["weather"][0]["description"])
    print("Скорость ветра: {} км/час".format(info["wind"]["speed"]))
    print("Направление ветра: ",info["wind"]["deg"])
    print("Относительная влажность: {} %".format(info["main"]["humidity"]))
    print("Атмосферное давление: {} ГПа".format(info["main"]["pressure"]))
    print("Температура воздуха: {} по Цельсию".format(int(info["main"]["temp_min"]-273)))
    
def remove_file_if_exist(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass
   

# выбираем страну из скачанного списка
my_country = choose_country() 
print("Страна: ", my_country[1])
if my_country:
    # выбираем город из скачанного списка выбранной страны
    my_city = choose_city(my_country[0])
    if my_city:
        get_weather_info(my_city, my_country)
        print("Информация записана в файл resilt.txt")
    else:
        print("Город не был выбран, заканчиваем работу")
else:
    print("Страна не была выбрана, заканчиваем работу")
    
choice = input("Почистить папку от файлов с информацией(Y/N)? :")
if choice:
    remove_file_if_exist("arch.gz")
    remove_file_if_exist("cities.json")
    remove_file_if_exist("countries.txt")

