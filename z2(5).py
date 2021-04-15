# задача 2 подзадача 5
def vvodfunc(s: str) -> int:
    bo = True
    print(s)
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


def zapros(mm: int, dd: dict):
    for ii in range(mm):
        ln: list = (input().split(" "))
        if not len(ln) == 2:
            print("Введён слишком длинный запрос")  # "read nya " Тоже
        else:
            if ln[1] not in d.keys():
                print("Такого файла нет!")
                continue
            else:
                if ln[0] not in ["execute", "read", "write"]:
                    print("Такого запроса нет!")
                else:
                    if ln[0] in dd[ln[1]]:
                        print("OK")
                    else:
                        print("Access denied")


def prove():
    bo = True
    while bo:
        snew = ""
        print("Введите имя файла и операции: ")
        ln: list = (input().split(" ", maxsplit=1))
        if len(ln) != 2:
            print("Ошибка ввода строки!")
        else:
            s = str(ln[1]).replace(" ", "")
            if not s.isalpha():
                print("Ошибка ввода операций!")
            elif len(s) > 4:
                print("Ошибка ввода операций!")
            else:
                for ii in range(len(s)):
                    if s[ii] == "X" or s[ii] == "W" or s[ii] == "R":
                        snew += s[ii] + " "
                    else:
                        print("Такой операции нет!")
                        snew = ""
                        break
                if len(snew) != 0:
                    ln[1] = snew[0:len(snew) - 1]
                    return ln


n = vvodfunc("Введите количество файлов: ")
d = {}
for i in range(n):
    l: list = prove()  # проверка
    l[1] = l[1].replace("X", "execute").replace("R", "read").replace("W", "write")
    d[l[0]] = l[1]
print(d)

m = vvodfunc("Введите количество запросов: ")
zapros(m, d)
