# Task_1
def func_favorite_movie(name):
    print(f"Мій улюблений фільм називається: {name}")
func_favorite_movie(input("Вкажіть назву Вашого улюбленого фільму: "))
# Task_2
def func_make_country(name, capital):
    country_dict = {'name': name, 'capital': capital}
    print(f"Назва країни: {country_dict['name']}, Столиця: {country_dict['capital']}")
func_make_country(input("Вкажіть назву країни: ").capitalize(), input("Вкажіть столицю: ").capitalize())
#Task_3
def func_make_operation(operator, *arguments):
    if not arguments:
        return 0
    result = arguments[0]
    if operator == '+':
        for num in arguments[1:]:
            result += num
    elif operator == '-':
        for num in arguments[1:]:
            result -= num
    elif operator == '*':
        for num in arguments[1:]:
            result *= num
    else:
        raise ValueError("оператор може бути '+', '-' или '*'")
    return result
print(func_make_operation('+', 7, 7, 2))
print(func_make_operation('-', 5, 5, -10, -20))
print(func_make_operation('*', 7, 6))
