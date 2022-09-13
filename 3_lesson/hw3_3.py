# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

raw = [1.1, 1.2, 3.1, 10.01]

def difference(list):
    i = 0
    min = 1
    max = 0
    while i < len(list):
        a = list[i]
        frac = a - int(a)
        if (frac < min):
            min = frac
        elif (frac > max):
            max = frac
        i += 1
    dif = max - min
    return round(dif,2)

print(difference(raw))