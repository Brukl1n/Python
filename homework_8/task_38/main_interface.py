print("Привет! Это программа телефонный справочник.\n")

print("Ниже описан функционал.\n")
print(" 1 - Добавить в справочник имя, фамилию и номер телефона\n 2 - Вывести на экран всё содержимое справочника")
print(" 3 - Найти человека в справочнике по фамилии\n 4 - Выход из программы\n")

print("Ниже описан дополнительный функционал.\n")
print(" 5 - Редактировать данные из справочника\n 6 - Удалить данные из справочника\n")

data_path = "Python/homework_8/task_38/extra_phonebook.txt"

while True:
    actions = int(input("Чтобы выполнить определённое действие из списка выше, введите его номер: "))
    print()
    match actions: 
        case 1: 
            import extra_input
            extra_input.input_data(input("Введите имя: "), input("Введите фамилию: "), input("Введите номер телефона: "))
        case 2: 
            from extra_output import output_all
            output_all()
        case 3:
            from extra_output import search_by_last_name
            search_by_last_name(input("Введите фамилию: "))
        case 4:
            break
        case 5:
            from extra_editing import data_editing
            data_editing(input("Введите номер телефона человека, чьи данные вы хотите отредактировать: "))
        case 6:
            from extra_editing import data_remove
            data_remove(input("Введите номер телефона человека, чьи данные вы хотите удалить: "))