# Напишите программу, которая по заданному номеру четверти, показывает...
# диапазон возможных координат точек в этой четверти (x и y).

q = int(input("Введите номер четверти: "))
if q == 1:
    print("X > 0; Y > 0")
elif q == 2:
    print("X < 0; Y > 0")
elif q == 3:
    print("X < 0; Y < 0")
elif q == 4:
    print("X > 0; Y < 0")
else:
    print("Введите значения 1-4.")