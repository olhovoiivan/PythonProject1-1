#Task_1
def count_words():
    new_list_1 = "Кияни поспішають на роботу вранці, а студенти йдуть на пари."
    words = new_list_1.split()
    new_dict = {}
    for word in words:
        if word:
            new_dict[word] = new_dict.get(word, 0) + 1
    return new_dict
count_words()
print(f" Результат: {count_words()}")
#Task_2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def func_stock_value(stock, prices):
    stock_total_values = {}
    for item, quantity in stock.items():  # Метод items() повертає пари ключ-значення зі словника stock.
        # Наприклад, для "banana": item = "banana", quantity = 6.
        if item in prices:  # Перевірка наявності товару в словнику prices
            price = prices[item]  # Якщо товар є в prices, отримуємо його ціну
            total_value = quantity * price
            stock_total_values[item] = total_value
    return stock_total_values
item_values = func_stock_value(stock, prices)
print(f"Виводимо словник з вартостями всіх товарів: {item_values}")
# Метод item_values.values() повертає значення словника: [24.0, 0.0, 48.0, 45.0]
grand_total = sum(item_values.values())
print(f"Виводиться загальна вартість усіх товарів: {grand_total}")
#Task_3
list_tuples = [(i, i * i) for i in range(1, 11)]
print(f"Cписку, що містить кортежі: {list_tuples}")
#Task_4
# 1. Створення списка із днями тижня
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# 2. Створення словника {1: "Monday", 2: "Tuesday", ...}
day_dict = {index + 1: day for index, day in enumerate(weekdays)}
# 3. Створення зворотного словника {"Monday": 1, "Tuesday": 2, ...}
# Просто міняємо місцями ключ і значення з попереднього словника
num_dict = {day: num for num, day in day_dict.items()}
print(f"Список днів тижня: {weekdays}")
print(f"Розподіл днів за номерами: {day_dict}")
print(f"Розподіл номерів за днями: {num_dict}")

