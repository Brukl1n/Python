data_path = "Python/homework_8/task_38/extra_phonebook.txt"

def input_data(first_name, last_name, phone_number):
    with open(data_path, "a", encoding = "utf-8") as extra_phonebook:
        extra_phonebook.write(f"{first_name} : {last_name} : {phone_number} \n")
    print("\nИмя, фамилия и телефон добавлены в справочник. \n")

def input_data_editing(first_name, last_name, phone_number):
    with open(data_path, "a", encoding = "utf-8") as extra_phonebook:
        extra_phonebook.write(f"{first_name} : {last_name} : {phone_number} \n")
    print("\nИмя, фамилия и телефон отредактированы. \n")