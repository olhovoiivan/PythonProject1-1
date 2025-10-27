# Task_1
class Person():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def all_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Зріст: {self.height}, Вага: {self.weight}"

class Student(Person):
    def __init__(self, name, age, height, weight, grade_level):
        super().__init__(name, age, height, weight)
        self.grade_level = grade_level
        self.gpa = 0.0

    def calculate_gpa(self, grades):
        if grades:
            self.gpa = sum(grades) / len(grades)
            return f"Середній бал оновлено до {self.gpa:.2f}"
        return "Оцінки не надано"

    def promote(self):
        self.grade_level += 1
        return f"Переведено до класу {self.grade_level}"

class Teacher(Person):
    def __init__(self, name, age, height, weight, salary, subject):
        super().__init__(name, age, height, weight)
        self.salary = salary
        self.subject = subject

    def update_salary(self, new_salary):
        self.salary = new_salary
        return f"Зарплату оновлено до {self.salary}"

    def change_subject(self, new_subject):
        self.subject = new_subject
        return f"Предмет змінено на {self.subject}"

if __name__ == "__main__":
    student_1 = Student("Іван", 10, 130, 40, 5)
    teacher_1 = Teacher("Іван Сергійович", 40, 176, 100, 20000, "Біологія")



# Task_2
class Mathematician():
    def square_nums(self, numbers):
        # Повертає список квадратів чисел
        return [num ** 2 for num in numbers]

    def remove_positives(self, numbers):
        # Видаляє додатні числа зі списку
        return [num for num in numbers if num <= 0]

    def filter_leaps(self, years):
        # Фільтрує високосні роки
        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return [year for year in years if is_leap_year(year)]

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# Task_3
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        # Додаємо атрибут для зберігання оригінальної ціни (до націнки)
        self._original_price = price
        # Додаємо, щоб знати, чи застосована націнка
        self._is_marked_up = False

class ProductStore:
    def __init__(self):
        self.products = {}  # Словник {продукт: кількість}
        self.income = 0  # Загальний дохід

    def add(self, product, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Кількість має бути додатним цілим числом")
        # Перевіряємо, чи націнка вже застосована
        if not product._is_marked_up:
            # Якщо ні, застосовуємо націнку 30% і встановлюємо прапорець
            product.price *= 1.3
            product._is_marked_up = True
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        if not isinstance(percent, (int, float)) or percent < 0 or percent > 100:
            raise ValueError("Знижка має бути відсотком від 0 до 100")
        for product in self.products:
            if identifier_type == 'name' and product.name == identifier:
                product.price *= (1 - percent / 100)
            elif identifier_type == 'type' and product.type == identifier:
                product.price *= (1 - percent / 100)
            else:
                raise ValueError("Неправильний ідентифікатор або тип")

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name:
                if self.products[product] >= amount:
                    self.products[product] -= amount
                    self.income += product.price * amount
                    if self.products[product] == 0:
                        del self.products[product]
                    return
                else:
                    raise ValueError("Недостатня кількість продукту в магазині")
        raise ValueError("Продукт не знайдено")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return {f"{p.name} ({p.type})": qty for p, qty in self.products.items()}

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return (product.name, self.products[product])
        return (product_name, 0)

# Тестування
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)

# Task_4
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        # Записуємо повідомлення про помилку до файлу logs.txt
        with open('logs.txt', 'a') as file:
            file.write(f"Помилка: {msg}\n")

# Приклад використання
try:
    raise CustomException("Тестова помилка")
except CustomException as e:
    print(f"Виникла помилка: {e}")



