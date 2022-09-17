# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

my_raw = [1, 1, 2, 3, 4, 5, 6, 7, 7, 8] # -> [2,3,4,5,6]

def not_repeat(raw):
    list = []
    for i in range (0, len(raw)):
        count = raw.count(raw[i])
        if count > 1:
            continue
        else:
            list.append(raw[i])
    return list

print(not_repeat(my_raw))
