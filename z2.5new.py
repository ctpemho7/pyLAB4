filein = open('input2.txt', 'r', encoding="utf-8")
fileout = open('output2.txt', 'w', encoding="utf-8")

ind1 = ind2 = 0
line = filein.readlines()
try:
    ind1 = int(line[0])  # это количество файлов
    ind2 = int(line[1 + ind1])  # это количество запросов
except ValueError:
    print("Некорректный файл! Неверный формат количества запросов/файлов")
    fileout.write("Некорректный файл! Неверный формат количества запросов/файлов")
    exit()
except IndexError:
    print("Некорректный файл! Неверный ввод количества запросов/файлов")
    fileout.write("Некорректный файл! Неверный ввод количества запросов/файлов")
    exit()

if len(line) != 2 + ind1 + ind2:  # длина line равна количеству файлов+количество запросов + 2
    print("Некорректный ввод операций!")
    fileout.write("Некорректный ввод операций!")
    exit()

files: dict = {}
for i in range(1, ind1 + 1):  # построчная обработка

    split_line: list = line[i].split(' ', maxsplit=1)
    if len(split_line) != 2:  # две части у файла: имя и операции
        print("Ошибка ввода строки!")
        fileout.write("Ошибка ввода строки!")
        exit()

    name = str(split_line[0]).replace("    ", "")  # Убираем лишнее
    operations = str(split_line[1]).replace(" ", "").replace('\n', '')  # ==трока операций

    if not 0 < len(operations) < 4:  # Длина строки операций не превосходит 4 и != 0
        print('Некорректный ввод операций!')
        fileout.write("Некорректный ввод операций!")
        exit()

    for ii in range(len(operations)):  # Проверяем операции
        if not (operations[ii] == "X" or operations[ii] == "W" or operations[ii] == "R"):
            print("Такой операции нет!")
            fileout.write("Такой операции нет!")
            exit()

    operations = operations.replace("WWW", "W").replace("WW", "W").replace("W", "write ")  # Убираем лишнее
    operations = operations.replace("RRR", "R").replace("RR", "R").replace("R", "read ")
    operations = operations.replace("XXX", "X").replace("XX", "X").replace("X", "execute ")
    operations = operations[:-1]
    files[name] = operations  # всё в словарь

files_keys = list(files.keys())
files_values = list(files.values())

for zapros in range(ind1 + 2, len(line)):

    ask: list = str(line[zapros]).split(" ")  # вторая часть массива, в ней запросы

    if len(ask) != 2:  # все запросы состоят из 2 частей, разделённых пробелом
        print("Ошибка при вводе запроса!")
        fileout.write("Ошибка при вводе запроса!")
        exit()

    operation, name = ask[0], ask[1]
    name = name.replace('\n', '')  # Убираем всё лишнее

    if name not in files_keys:
        print("Такого файла нет!")
        fileout.write("Такого файла нет!")
        exit()

    if operation not in ["read", "write", "execute"]:
        print("Такого запроса нет!")
        fileout.write("Такого запроса нет!")
        exit()

    if operation in files[name]:
        fileout.write("OK\n")
    else:
        fileout.write("Access denied\n")

fileout.close()
filein.close()
