# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
num = 5
def polinomial(k):
    list = []
    while k >= 1:
        if k == 1:
            list.append(random.randint(0,100))
            list.append("x")
            list.append("+")
        else:
            rand = random.randint(0,100)
            if rand ==0:
                list.append(0)
            else:
                list.append(rand)
                list.append("*")
                list.append("x^")
                list.append(k)
                list.append("+")

        k -= 1
    list.append(random.randint(0,100))
    list.append("=")
    list.append(0)


    return list

raw = polinomial(num)
print(*raw, sep=" ")