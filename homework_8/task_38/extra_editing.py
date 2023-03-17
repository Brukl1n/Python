import re
import extra_input
from extra_output import search_by_phone_number

data_path = "Python/homework_8/task_38/extra_phonebook.txt"

def data_remove(phone_number):
    with open(data_path, "r", encoding = "utf-8") as extra_phonebook:
        lines = extra_phonebook.readlines()

    str = phone_number
    pattern = re.compile(re.escape(str))

    with open(data_path, "w", encoding = "utf-8") as extra_phonebook:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                extra_phonebook.write(line)
    print()

def data_editing(phone_number):
        extra_input.input_data_editing(input("Введите новое имя: "), input("Введите новую фамилию: "), input("Введите новый номер телефона: "))
        data_remove(phone_number)