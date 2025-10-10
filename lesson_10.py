# Task_1
def func_oops():
    lst = [1, 2, 3]
    return lst[5]  # IndexError
def func_oops_one():
    try:
        func_oops()
    except IndexError:
        print("Помилка: Індекс поза межами списку!")
func_oops_one()
'''
Якщо ви зміните функцію func_oops так, щоб вона викликала KeyError замість 
IndexError, то виняток не буде перехоплено. Це станеться тому, що блок except 
у функції func_oops_one налаштований лише на перехоплення IndexError
'''
# Task_2_A
def func_math():
    try:
        a = int(input('Вкажіть, будь ласка, перше значення: '))
        b = int(input('Вкажіть, будь ласка, друге значення: '))
        c = a**2 / b
        return c
    except ZeroDivisionError:
        print("Ділення на нуль неможливе!")
        return None  # Повертаємо None у разі помилки
    except ValueError:
        print("Введіть коректне число!")
        return None  # Повертаємо None у разі помилки
result = func_math()
if result is not None:
    print(f"Результат: {result}")
# Task_2_B
def func_math():
    while True:
        try:
            a = int(input('Вкажіть, будь ласка, перше значення: '))
            b = int(input('Вкажіть, будь ласка, друге значення: '))
            c = a**2 / b
            return c
        except ZeroDivisionError:
            print("Ділення на нуль неможливе! Спробуйте ще раз.")
        except ValueError:
            print("Введіть коректне число! Спробуйте ще раз.")
result = func_math()
print(f"Результат: {result}")
