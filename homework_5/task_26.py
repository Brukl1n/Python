# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

print("Привет! Эта программа принимает на вход два числа A и B, и возводит число А в целую степень B.")
print()

def exponentiation(first_number, second_number):
    if second_number == 0:
        return 1
    if second_number < 0:
        return 1 / exponentiation(first_number, -second_number)
    if second_number % 2 == 0:
        return exponentiation(first_number, second_number // 2) * exponentiation(first_number, second_number // 2)
    else:
        return exponentiation(first_number, second_number - 1) * first_number

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print()

print(exponentiation(A, B))