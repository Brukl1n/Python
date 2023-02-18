# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

print("Привет! Эта программа проверяет является ли введённый билет счастливым.")
print()

verifiableTicket = int(input("Введите шестизначный номер билета: "))
num6 = 0
num5 = 0
num4 = 0
num3 = 0
num2 = 0
num1 = 0
firstHalf = 0
secondHalf = 0

if verifiableTicket < 100000 or verifiableTicket > 999999:
    print()
    print("Введённый билет не является шестизначным!")
else:
    num6 = verifiableTicket % 10
    num5 = verifiableTicket // 10 % 10
    num4 = verifiableTicket // 100 % 10
    num3 = verifiableTicket // 1000 % 10
    num2 = verifiableTicket // 10000 % 10
    num1 = verifiableTicket // 100000 % 10
    firstHalf = num1 + num2 + num3
    secondHalf = num4 + num5  + num6

if firstHalf != secondHalf:
    print()
    print("Билет не является счастливым :(")
else:
    print()
    print("Билет является счастливым :)")