# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

#   НЕ РЕШИЛА. VS Code не знает библиотеку sympy (((. А PyCharm настроить не получается.

a = open("1.txt", "w")
a.writelines("3+5=8")
a.close

num1 = []
a = open('1.txt', 'r')
for i in a:
    num1.append(i)
print(num1)

b = open("2.txt", "w")
b.writelines("4+6=10")
b.close

num2 = []
b = open('2.txt', 'r')
for i in b:
    num2.append(i)
print(num2)

