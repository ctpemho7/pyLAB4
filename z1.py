s = input().replace('!', '').replace('?', '').replace('.', '').replace(',', '').replace(':', '').\
                                                                                             replace(';', '')
lst = s.split()
set1 = set(lst)
if len(set1) == 0:
    print("Ошибка ввода строки! Программа не принимает на вход знаки препинания")
else:
    for elem in set1:
        print("Вхождений слова «" + elem + "» в исходную строку составляет " + str(lst.count(elem)) + " раз(а)")
