# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Введите число: "))
i = 1
sum = 0
while i <= k:
    a = (1+1/i)**i
    sum = sum+a
    print(round(a,2))
    i += 1
    # print(sum)
print("Общая сумма = ", round(sum,2))