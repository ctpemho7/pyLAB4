import json
from pprint import pprint


def js():
    # Serializing json
    json_object = json.dumps(dict_data, indent=4, ensure_ascii=False)

    # Writing to sample.json
    with open("database.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_object)

    # Reading from json file
#    with open('database.json', 'r', encoding="utf-8") as openfile:
#        json_object = json.load(openfile)


dict_data = {
    "Самолеты":
        [
            {
                "id": 1,  # в id связка между пассажиром и самолётом
                "Номер": 777,
                "Модель": "Airbus",
                "Маршрут": "Тель-Авив -> Нур-Султан",
                "Дата ТО": "09.02.2017"
            },
            {
                "id": 2,
                "Номер": 12378,
                "Модель": "Airbus",
                "Маршрут": "Пермь -> Рейкьявик",
                "Дата ТО": "10.07.2019"
            }
        ],

    "Пассажиры":
        [{
            "ФИО": "Иванова Г.И.",
            "История":
                [{
                    "id": 1,  # к id самолёта привязан пассажир
                    "Дата полета": "15.04.2020",
                    "Место": 152
                }]
        },
            {
                "ФИО": "Александров Е.А.",
                "История":
                    [{
                        "id": 2,  # к id самолёта привязан пассажир
                        "Дата полета": "13.07.2021",
                        "Место": 18
                    }]
            }

        ]

}


def text_menu():
    print("1. Добавить самолёт\n"
          "2. Добавить пассажира\n"
          "3. Добавить перелёт в историю пассажира\n"
          "4. Вывести информацию об самолёте\n"
          "5. Вывести информацию о пассажире\n"
          "6. Удалить самолёт из базы данных\n"
          "7. Удалить пассажира из базы данных\n"
          "8. Удалить самолёт из истории пассажира\n"
          "9. Изменить данные самолёта\n"
          "10. Изменить данные пассажира\n"
          "11. Выход")


def check_uint() -> int:
    bo = True
    while bo:
        try:
            nn = int(input())
        except ValueError:
            print('Введено не натуральное число!')
        else:
            if not nn > 0:
                print("Введено отрицательное число или ноль!")
            else:
                return nn


def set_date():
    month = year = day = 0
    DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    check = True
    while check:
        print("Введите год: ")
        year = check_uint()
        if not 1970 <= year <= 9999:
            print("Введите корректный год!")
        else:
            check = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        DAYS_IN_MONTH[2] = 29

    check = True
    while check:
        print("Введите номер месяца от 1 до 12: ")
        month = check_uint()
        if not 1 <= month <= 12:
            print("Введите корректный месяц!")
        else:
            check = False
    s_month = str(month)
    if len(s_month) != 2:
        s_month = '0' + str(month)

    days_in_month = DAYS_IN_MONTH[month]
    check = True
    while check:
        print("Введите день месяца: ")
        day = check_uint()
        if not 1 <= day <= days_in_month:
            print("Введите корректный день!")
        else:
            check = False

    s_day = str(day)
    if len(s_day) != 2:
        s_day = '0' + str(day)

    return s_day + '.' + s_month + '.' + str(year)


def available_ids() -> list:
    lst = []
    for elem_id in dict_data["Самолеты"]:
        lst.append(elem_id["id"])
    return lst


def add_plane():
    d = {}
    bo, planeId = True, 0
    while bo:
        listOfIds = available_ids()
        print("Введите новый id самолёта, недоступны следующие id:")
        print(listOfIds)
        planeId = check_uint()
        if planeId in listOfIds:
            print("Такой id уже есть!")
        else:
            bo = False

    print("Введите номер самолёта: ")
    number = check_uint()
    model = input("Введите название модели самолёта: ")
    fromm = input("Введите название города отправления: ")
    to = input("Введите название города назначения: ")
    path = fromm + " -> " + to
    print("Укажите дату ТО: ")
    dateTO = set_date()

    d["id"] = planeId
    d["Номер"] = number
    d["Модель"] = model
    d["Маршрут"] = path
    d["Дата ТО"] = dateTO

    dict_data["Самолеты"].append(d)
    js()


def add_passenger():
    d = {}

    fio = input("Введите ФИО пасссажира: ")
    bo, passId = True, 0
    while bo:
        listOfIds = available_ids()
        print("Введите id самолёта, на котором летит пассажир. Вот эти id:")
        print(listOfIds)
        passId = check_uint()
        if passId not in listOfIds:
            print("Такого id нет!")
        else:
            bo = False

    print("Укажите дату полёта: ")
    flightDate = set_date()

    print("Укажите место в самолёте: ")
    place = check_uint()

    history = [{
            "id": passId,
            "Дата полета": flightDate,
            "Место": place
            }]

    d["ФИО"] = fio
    d["История"] = history

    dict_data["Пассажиры"].append(d)
    js()


def add_history():
    all_passengers = dict_data["Пассажиры"]
    fio_passengers = []
    print("Список всех пассажиров: ")  # Печать всех пассажиров
    for elem in all_passengers:
        pprint(elem["ФИО"])
        fio_passengers.append(elem["ФИО"])

    # Ввод фамилии
    bo, ind = True, -1
    while bo:
        fio = input("Введите ФИО пассажира: ")
        for i in range(len(fio_passengers)):
            if fio == fio_passengers[i]:
                ind = i
                bo = False
                break
        if ind == -1:
            print("Такого ФИО нет!")

    bo, passId = True, 0
    while bo:  # Ввод ID для самолёта
        listOfIds = available_ids()
        print("Введите id самолёта, на котором летит пассажир. Вот эти id:")
        print(listOfIds)
        passId = check_uint()
        if passId not in listOfIds:
            print("Такого id нет!")
        else:
            bo = False

    print("Укажите дату полёта: ")
    flightDate = set_date()

    print("Укажите место в самолёте: ")
    place = check_uint()

    history = {
            "id": passId,
            "Дата полета": flightDate,
            "Место": place
            }
    n = list(dict_data["Пассажиры"][ind]["История"])
    n.append(history)
    dict_data["Пассажиры"][ind]["История"] = n
    js()


def show_plane():
    bo, sh = True, 0
    listOfIds = available_ids()
    while bo:
        print("Выберите нужный самолёт: ")
        print(listOfIds)
        sh = check_uint()
        if sh not in listOfIds:
            print("Такого самолёта нет!")
        else:
            bo = False

    sh = listOfIds.index(sh)  # костыль для правильного определения индекса
    pprint(dict_data["Самолеты"][sh])


def show_pass():

    all_passengers = dict_data["Пассажиры"]
    fio_passengers = []
    print("Список всех пассажиров: ")  # Печать всех пассажиров
    for elem in all_passengers:
        pprint(elem["ФИО"])
        fio_passengers.append(elem["ФИО"])
    count = 0
    fio = input("Введите ФИО пассажира: ")
    for elem in all_passengers:
        if elem["ФИО"] == fio:
            pprint(elem)
            count = 1
    if not count:
        print("Таких пассажиров нет!")


def del_plane():
    bo, sh = True, 0
    listOfIds = available_ids()
    while bo:
        print("Выберите нужный самолёт: ")
        print(listOfIds)
        sh = check_uint()
        if sh not in listOfIds:
            print("Такого самолёта нет!")
        else:
            bo = False

    sh = listOfIds.index(sh)  # костыль для правильного определения индекса
    deli = dict_data["Самолеты"][sh]
    dict_data["Самолеты"].remove(deli)
    js()


def del_passenger():
    all_passengers = dict_data["Пассажиры"]
    fio_passengers = []
    print("Список всех пассажиров: ")  # Печать всех пассажиров
    for elem in all_passengers:
        pprint(elem["ФИО"])
        fio_passengers.append(elem["ФИО"])

    # Ввод фамилии
    bo, ind = True, -1
    while bo:
        fio = input("Введите ФИО пассажира: ")
        for i in range(len(fio_passengers)):
            if fio == fio_passengers[i]:
                ind = i
                bo = False
                break
        if ind == -1:
            print("Такого ФИО нет!")

    deli = dict_data["Пассажиры"][ind]
    dict_data["Пассажиры"].remove(deli)
    js()


def del_history():
    all_passengers = dict_data["Пассажиры"]
    fio_passengers = []
    print("Список всех пассажиров: ")  # Печать всех пассажиров
    for elem in all_passengers:
        pprint(elem["ФИО"])
        fio_passengers.append(elem["ФИО"])

    # Ввод фамилии
    bo, ind = True, -1
    while bo:
        fio = input("Введите ФИО пассажира: ")
        for i in range(len(fio_passengers)):
            if fio == fio_passengers[i]:
                ind = i
                bo = False
                break
        if ind == -1:
            print("Такого ФИО нет!")

    history_list = ["000"]  # заполняем лист и тут же его печатаем, "000" нужен для корректного отображения
    print("История полётов этого пассажира: ")
    for i in range(len(dict_data["Пассажиры"][ind]["История"])):
        history_list.append(dict_data["Пассажиры"][ind]["История"][i])
        print(str(i+1) + " " + str(history_list[i+1]))

    if len(history_list) == 1:
        print("Нет истории, нечего удалять!")
    else:
        print("Введите значение, которое нужно удалить: ")
        bo, n = True, -1
        while bo:
            n = check_uint()
            if n > len(history_list):
                print("Такого индекса нет!")
            else:
                bo = False

        history_list.remove(history_list[n])
        history_list.remove("000")
        dict_data["Пассажиры"][ind]["История"] = history_list
        js()


def edit_plane():
    bo, sh = True, 0
    listOfIds = available_ids()
    while bo:
        print("Выберите нужный самолёт: ")
        print(listOfIds)
        sh = check_uint()
        if sh not in listOfIds:
            print("Такого самолёта нет!")
        else:
            bo = False

    sh = listOfIds.index(sh)  # костыль для правильного определения индекса
    print("Данные этого самолёта: ")
    pprint(dict_data["Самолеты"][sh])
    keys = ["Дата ТО", "Маршрут", "Модель", "Номер"]

    bo, key = True, ""
    while bo:
        key = input("Введите ключ для изменения: ")
        if key not in keys:
            print("Такого ключа нет!")
        else:
            bo = False

    print("Введите новое значение поля: ")
    value = ""
    if key == "Дата ТО":
        value = set_date()
    if key == "Маршрут":
        fromm = input("Введите название города отправления: ")
        to = input("Введите название города назначения: ")
        value = fromm + " -> " + to
    if key == "Модель":
        value = input()
    if key == "Номер":
        value = check_uint()

    dict_data["Самолеты"][sh][key] = value
    js()


def edit_passenger():
    print("Вы можете изменить ФИО пассажира: ")
    all_passengers = dict_data["Пассажиры"]
    fio_passengers = []
    print("Список всех пассажиров: ")  # Печать всех пассажиров
    for elem in all_passengers:
        pprint(elem["ФИО"])
        fio_passengers.append(elem["ФИО"])

    # Ввод фамилии
    bo, ind = True, -1
    while bo:
        fio = input("Введите ФИО пассажира: ")
        for i in range(len(fio_passengers)):
            if fio == fio_passengers[i]:
                ind = i
                bo = False
                break
        if ind == -1:
            print("Такого ФИО нет!")

    new_fio = input("Введите новое ФИО: ")
    dict_data["Пассажиры"][ind]["ФИО"] = new_fio
    js()


js()
fist = True
while fist:
    if len(dict_data["Самолеты"]) != 0 and len(dict_data["Пассажиры"]) != 0:
        text_menu()
        menu = check_uint()

        if menu == 1:
            add_plane()
        if menu == 2:
            add_passenger()
        if menu == 3:
            add_history()
        if menu == 4:
            show_plane()
        if menu == 5:
            show_pass()
        if menu == 6:
            del_plane()
        if menu == 7:
            del_passenger()
        if menu == 8:
            del_history()
        if menu == 9:
            edit_plane()
        if menu == 10:
            edit_passenger()
        if menu == 11:
            exit()
        elif not 1 <= menu <= 11:
            print('Некорректный ввод')

    else:
        print("Пустая база данных! Добавьте недостающие поля для продолжения работы")
        if len(dict_data["Самолеты"]) == 0:
            print("1. Добавить самолёт\n"
                  "2. Выход")
            menu = check_uint()
            if menu == 1:
                add_plane()
            if menu == 2:
                exit()
            elif not 1 <= menu <= 2:
                print('Некорректный ввод')

        elif len(dict_data["Пассажиры"]) == 0:
            print("1. Добавить пассажира\n"
                  "2. Выход")
            menu = check_uint()
            if menu == 1:
                add_passenger()
            if menu == 2:
                exit()
            elif not 1 <= menu <= 2:
                print('Некорректный ввод')
