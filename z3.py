from pprint import pprint
from random import randint


def text_menu_dict():
    print("1. Задать новые случайные значения словаря\n"
          "2. Добавить элемент словаря\n"
          "3. Вывести словарь при помощи pprint\n"
          "4. Вывести ключи с наибольшим, наименьшим значением и общее среднее значение\n"
          "5. Удаление элемента по его ключу\n"
          "6. Перейти к работе со списком словарей\n"
          "7. Выход")


def text_menu_dict_small():
    print("1. Задать новые случайные значения словаря\n"
          "2. Добавить элемент словаря\n"
          "3. Выход")


def text_menu_list():
    print("1. Вывести список при помощи pprint\n"
          "2. Сортировка списка по значениям при помощи лямбда функции\n"
          "3. Сортировка списка по ключам при помощи лямбда функции\n"
          "4. Задать значение элемента по введенному ключу\n"
          "5. Вывести на экран ключи с одинаковыми значениями\n"
          "6. Выход")


def int_func() -> int:
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


airports = ["Внуково", "Домодедово", "Торонто", "Дубай", "Токио",
            "Лондон", "Лос-Анжелес", "Пекин", "Хельсинки", "Гонконг",
            "Франкфурт", "Стамбул", "Сингапур", "Дели", "Лас Вегас"]


def rnd_dict(dd: dict):  # 1
    for i in range(15):
        dd[airports[i]] = randint(10000, 110000)


def fill_dict(dd: dict):  # 2
    key = input("Введите значение ключа: ")
    print("Введите значение пассажиропотока: ")
    value = int_func()
    dd[key] = value


def max_min_avr(dd: dict):  # 4
    maxi = max(dd, key=dd.get)
    minn = min(dd, key=dd.get)
    print("Максимальное значение в аэропорте ", maxi, ":", dd[maxi], sep=' ')
    print("Минимальное значение в аэропорте", minn, ":", dd[minn], sep=' ')
    all_sum = 0
    for i in dd.keys():
        all_sum = all_sum + dd[i]
    print("Средний пассажиропоток составляет:", round(all_sum / len(dd)), sep=' ')


def pop_dict(dd: dict):  # 5
    key = input("Введите значение ключа: ")
    if key not in dd.keys():
        print("Такого ключа нет!")
    else:
        dd.pop(key)


def create_list(dd: dict):  # 1list
    ll = []
    for key, value in dd.items():
        ff = {'key': key,
              'value': value}
        ll.append(ff)
    return ll


def sort_list_value(ll: list):  # 2list
    ll.sort(key=lambda x: x['value'])  # свой порядок сортировки
    pprint(ll)


def sort_list_key(ll: list):  # 2list
    ll.sort(key=lambda x: x['key'])  # свой порядок сортировки
    pprint(ll)


def fill_list(ll: list):  # 3list
    key = input("Введите значение ключа: ")
    print("Введите значение пассажиропотока: ")
    value = int_func()
    ff = {'key': key,
          'value': value}
    ll.append(ff)
    pprint(ll)


def find_the_same_values_in_list(param_list: list):
    print("Введите значение, ключи которого нужно найти: ")
    find = int_func()
    keys = list()
    for index in range(len(param_list)):
        new_second = list(param_list[index].values())
        keys.append(new_second)
    founded = dict()
    for mas_index in range(len(keys)):
        if find == keys[mas_index][1]:
            founded[keys[mas_index][0]] = keys[mas_index][1]
    if len(founded) == 0:
        print("Ключей с таким значением нет!")
    else:
        print("Обнаружены следующие значения: ")
        pprint(founded)


d = {}
lst = list()
fist = True
list_menu = False
while fist:
    if len(d) == 0:
        text_menu_dict_small()
        menu = int_func()
        if menu == 1:
            rnd_dict(d)
        if menu == 2:
            fill_dict(d)
        if menu == 3:
            exit()
        elif not 1 <= menu <= 3:
            print('Некорректный ввод')
    else:
        text_menu_dict()
        menu = int_func()
        if menu == 1:
            rnd_dict(d)
        if menu == 2:
            fill_dict(d)
        if menu == 3:
            pprint(d)
        if menu == 4:
            max_min_avr(d)
        if menu == 5:
            pop_dict(d)
        if menu == 6:
            list_menu = True
            lst = create_list(d)
        if menu == 7:
            exit()
        elif not 1 <= menu <= 7:
            print('Некорректный ввод')

    while list_menu:
        text_menu_list()
        menu = int_func()
        if menu == 1:
            pprint(lst)
        if menu == 2:
            sort_list_value(lst)
        if menu == 3:
            sort_list_key(lst)
        if menu == 4:
            fill_list(lst)
        if menu == 5:
            find_the_same_values_in_list(lst)
        if menu == 6:
            exit()
        elif not 1 <= menu <= 6:
            print('Некорректный ввод')
