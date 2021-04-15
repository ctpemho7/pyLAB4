def prove(s: str):
    sp = s.split(": ")
    if len(sp) == 2 and sp[0].isalpha() and sp[1].replace("\n", "").isdigit():
        return True
    else:
        return False


try:
    f = open('results.txt', 'r', encoding="utf-8")
    fileout = open('output.txt', 'w+')
except FileNotFoundError:
    print("Создайте файл!")
    exit()

d = {}
line = f.readline()
while line:
    if prove(line):
        l = list(line.split(": "))
        l[1] = int(l[1])
        d[l[0]] = l[1]
        line = f.readline()
    else:
        print("Ошибка в строке!")
        exit()

list_items = list(d.items())
list_items.sort(key=lambda elem: elem[1], reverse=True)

for i in range (len(list_items)):
    tuple: list = list(list_items[i])
    s = str(tuple[0]) + ": " + str(tuple[1]) + "\n"
    fileout.writelines(s)
f.close()
fileout.close()
