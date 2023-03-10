# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

print("Привет! Эта программа определяет индексы элементов списка, значения которых пренадлежат заданному диапазону.")
print()

array = []
array_length = int(input("Введите длину списка: "))

for i in range(array_length):
    array.append(randint(-10, 10))

print(f"Сгенерированный список: {array}")
print()

minimum_number = int(input("Введите минимум диапазона: "))
maximum_number = int(input("Введите максимум диапазона: "))

for i in range(array_length):
    if minimum_number <= array[i] <= maximum_number:
        print(i)