# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = 80

def bin(a):
    list = [] 
    while a >= 1: 
        ost = a % 2
        list.append(ost)
        a = int(a/2)
    list.reverse()
    return list

print(bin(num))

