# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
control_number = int(input("Введите число: "))
digree = 1
while (digree < control_number):
    print(digree)
    digree *= 2
