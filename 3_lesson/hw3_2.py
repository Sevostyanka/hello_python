# # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# # второй и предпоследний и т.д.
# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

list = [2,3,4,5,6,7,8]
list2 = [2,3,4,5,6,7]

def multList(a):
    list = []
    i = 0
    if len(a) % 2 == 0:
        while i < int(len(a)/2):
            list.append(a[i]*a[((i+1)*(-1))])
            i +=1
    if len(a) % 2 > 0:
        while i <= int(len(a)/2):
            list.append(a[i]*a[((i+1)*(-1))])
            i +=1
    return list

print(multList(list))
print(multList(list2))