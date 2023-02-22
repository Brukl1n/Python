# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

print("Привет! Эта программа выводит все степени двойки, не превосходящие числа N.")
print()

numberN = int(input("Введите число N: "))
product = 0
degree = 1

while product * 2 < numberN:
    product = 2 ** degree
    print(f"2^{degree} = {product}")
    degree += 1