data_path = "Python/homework_8/task_38/extra_phonebook.txt"

def output_all():
    with open(data_path, "r", encoding = "utf-8") as extra_phonebook:
        for line in extra_phonebook:
            print(line)
       
def search_by_last_name(last_name):
    last_name = last_name.lower()
    with open(data_path, "r", encoding = "utf-8") as extra_phonebook:
        flag = False
        for line in extra_phonebook:
            if last_name in line.lower():
                print()
                print(line)
                flag = True
        if flag == False:
            print()
            print("Такого человека нет в справочнике \n")

def search_by_phone_number(phone_number):
    phone_number = phone_number.lower()
    with open(data_path, "r", encoding = "utf-8") as extra_phonebook:
        flag = False
        for line in extra_phonebook:
            if phone_number in line.lower():
                print()
                print(f"Данные человека, которые вы хотите отредактировать: {line}")
                flag = True
        if flag == False:
            print()
            print("Такого человека нет в справочнике \n")