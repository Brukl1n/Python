# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.

# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

print("Привет! Эта программа вычисляет стоимость введённого русского или английского слова в игре Scrabble.")
print()

PointsEng1 = ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R")
PointsEng2 = ("D", "G")
PointsEng3 = ("B", "C", "M", "P")
PointsEng4 = ("F", "H", "V", "W", "Y")
PointsEng5 = ("K")
PointsEng8 = ("J", "X")
PointsEng10 = ("Q", "Z")

PointsRus1 = ("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т")
PointsRus2 = ("Д", "К", "Л", "М", "П", "У")
PointsRus3 = ("Б", "Г", "Ё", "Ь", "Я")
PointsRus4 = ("Й", "Ы")
PointsRus5 = ("Ж", "З", "Х", "Ц", "Ч")
PointsRus8 = ("Ш", "Э", "Ю")
PointsRus10 = ("Ф", "Щ", "Ъ")

word = input("Введите слово на русском или английском языке: ")
print()
word = word.upper()
word = list(word)

print(f"Буквы из ведённого слова: {word}")
print()

result = 0

for i in range(len(word)):
    if word[i] in PointsEng1 or word[i] in PointsRus1:
        result += 1
    elif word[i] in PointsEng2 or word[i] in PointsRus2:
        result += 2
    elif word[i] in PointsEng3 or word[i] in PointsRus3:
        result += 3
    elif word[i] in PointsEng4 or word[i] in PointsRus4:
        result += 4
    elif word[i] in PointsEng5 or word[i] in PointsRus5:
        result += 5
    elif word[i] in PointsEng8 or word[i] in PointsRus8:
        result += 8
    elif word[i] in PointsEng10 or word[i] in PointsRus10:
        result += 10

print(f"Ваш результат: {result} очков!")