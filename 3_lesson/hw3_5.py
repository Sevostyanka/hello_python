# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = 8
list = [0,1]
def fib(a):
    if a > -1:
        if a == 0:
            return 0
        elif a ==1:
            return 1
        else:
            return fib(a-1) + fib(a-2)
    if a <= -1:
        return ((-1)**(a+1)) + fib(a)
    

for i in range(2,n+1):
    list.append(fib(i))

for i in range(1,n):
    list.insert(0,list[i+i])

ind = list.index(0)

i = ind+1
while i >= 0:
    list[i] = list[i]*(-1)
    i -= 2

print(list)
