# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

# Первый вариант решения задачи с выводом двух наборов чисел отдельо

print("Привет! Эта программа берёт два неупорядоченных набора целых чисел и выдаёт без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.")
print()

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
print()

firstList = []
secondList = []

resultFirstList = []
resultSecondList = []

i = 0
while i < n:
    firstList.append(random.randint(1, 21))
    i += 1
print(f"Первый набор чисел: {firstList}")

i = 0
while i < m:
    secondList.append(random.randint(1, 21))
    i += 1
print(f"Второй набор чисел: {secondList}")
print()

for j in range(len(firstList)):
    for k in range(len(firstList) - 1):
        if firstList[k] > firstList[k + 1]:
            firstList[k], firstList[k + 1] = firstList[k + 1], firstList[k]
print(f"Упорядоченный первый набор чисел: {firstList}")

for j in range(len(secondList)):
    for k in range(len(secondList) - 1):
        if secondList[k] > secondList[k + 1]:
            secondList[k], secondList[k + 1] = secondList[k + 1], secondList[k]
print(f"Упорядоченный второй набор чисел: {secondList}")
print()

resultFirstList.append(firstList[0])
i = 1
while i < n:
    if firstList[i] != firstList[i - 1]:
        resultFirstList.append(firstList[i])
    i += 1
print(f"Итоговый первый набор чисел: {resultFirstList}")

resultSecondList.append(secondList[0])
i = 1
while i < n:
    if secondList[i] != secondList[i - 1]:
        resultSecondList.append(secondList[i])
    i += 1
print(f"Итоговый первый набор чисел: {resultSecondList}")

# Второй вариант решения задачи с выводом общего набора чисел

# print("Привет! Эта программа берёт два неупорядоченных набора целых чисел и выдаёт без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.")
# print()

# n = int(input("Введите число n: "))
# m = int(input("Введите число m: "))
# print()

# firstList = []
# secondList = []
# resultList = []

# i = 0
# while i < n:
#     firstList.append(random.randint(1, 21))
#     i += 1
# print(f"Первый набор чисел: {firstList}")

# i = 0
# while i < m:
#     secondList.append(random.randint(1, 21))
#     i += 1
# print(f"Второй набор чисел: {secondList}")
# print()

# gluedltList = firstList + secondList
# print(f"Общий набор чисел: {gluedltList}")
# print()

# for j in range(len(gluedltList)):
#     for k in range(len(gluedltList) - 1):
#         if gluedltList[k] > gluedltList[k + 1]:
#             gluedltList[k], gluedltList[k + 1] = gluedltList[k + 1], gluedltList[k]
# print(f"Упорядоченный общий набор чисел: {gluedltList}")
# print()

# resultList.append(gluedltList[0])
# i = 1
# while i < n + m:
#     if gluedltList[i] != gluedltList[i - 1]:
#         resultList.append(gluedltList[i])
#     i += 1
# print(f"Итоговый общий набор чисел: {resultList}")