#Task_1
new_str = input("Вкажіть необхідний рядок: ")
def func_str(new_str):
    if len(new_str) < 2:
        return " "
    return new_str[:2] + new_str[-2:]
print(func_str(new_str))
#Task_2
phone_number = input("Вкажіть номер телефону: ")
def func_phone_number(phone):
    if len(phone) == 10 and phone.isdigit():
        return "Номер телефону вказан в правильному формату."
    return "Номер телефону вказан в НЕ правильному формату!"
print(func_phone_number(phone_number))
#Task_3
def func_math():
    correct_answer = 4
    user_answer = int(input("Вкажіть скільки буде 2*2? "))
    if user_answer == correct_answer:
        print("Вірно! Ви знаєте таблицю множення!")
    else:
        print(f"НЕВІРНО! Вірна відповідь {correct_answer}. Або я щось не те запрограмував.")
func_math()
#Task_4
def check_name():
    start_name = "anton"
    user_name = input("Вкажіть Ваше ім'я: ")
    if user_name.lower() == start_name:
        print("True: Вітаю, Антон!")
    else:
        print("False: Вітаю, а де Антон?")
check_name()
