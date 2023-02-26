# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random #мы ещё не затрагивали в обучении этот модуль, но так как он не влияет на сложность решения задачи то я решил включить его в программу

print("Привет! Эта программа находит в массиве самый близкий по величине элемент к заданному числу X.")
print()

A = []
i = 0
N = int(input("Введите число N: "))
print()

while i < N:
    A.append(random.randint(0, 10))
    i += 1

print(f"Сгенерированный массив: {A}")
print()

X = int(input("Введите число X от 1 до 10: "))
print()

d_Ain = sum(A)
k = 0

for k in A:
    if abs(X-k) < d_Ain:
        d_Ain = abs(X-k)
        i_Ain = k

print(f'Самый близкий по величине элемент к числу {X}: {i_Ain}.')