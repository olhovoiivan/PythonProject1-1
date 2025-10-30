# Task_1
class Animal():
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplemented('Must be implemented by a sub class')

class Cat(Animal):
    def talk(self):
        print('няв-няв')

class Dog(Animal):
    def talk(self):
        print('гав-гав')

def make_animal_talk(some_animal: Animal):
   print(f"Тваринка - {some_animal.name} видає звук: " , end='')
    some_animal.talk()

# Перевірка
cat_1 = Cat('Бусінка')
dog_1 = Dog('Пес')

make_animal_talk(cat_1)
make_animal_talk(dog_1)

# Task_2
class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = [] 

    def __str__(self):
        """Зручне для читання представлення (для користувача)."""
        return f"Автор: {self.name} ({self.country}, нар. {self.birthday})"

    def __repr__(self):
        """Офіційне представлення (для розробника)."""
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}', books={len(self.books)} книг)"

class Book:
    """ Представляє книгу."""
    total_books = 0  
    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        # Додаємо книгу до списку книг автора
        self.author.books.append(self)
        # Збільшуємо загальну кількість книг
        Book.total_books += 1

    def __str__(self):
        return f"Книга: '{self.name}' ({self.year}) | Автор: {self.author.name}"

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = [] 
        self.authors = set()  # Використовуємо set для уникнення дублікатів авторів

    def __str__(self):
        return f"Бібліотека '{self.name}'. Книг: {len(self.books)}, Авторів: {len(self.authors)}"

    def __repr__(self):
        return f"Library(name='{self.name}', total_books={len(self.books)}, total_authors={len(self.authors)})"

    def new_book(self, name: str, year: int, author: Author) -> Book:
        new_book_instance = Book(name, year, author)
        self.books.append(new_book_instance)
        self.authors.add(author)
        return new_book_instance

    def group_by_author(self, author: Author) -> list[Book]:
        return author.books

    # Task_3
from math import gcd

class Fraction():
    def __init__(self, numerator: int, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Чисельник і знаменник мають бути цілими числами")
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем")
        self._simplify()

    def _simplify(self):
        if self.denominator < 0:
        self.numerator = -self.numerator
        self.denominator = -self.denominator
        common_gcd = gcd(abs(self.numerator), self.denominator)
        self.numerator //= common_gcd
        self.denominator //= common_gcd

    def __add__(self, other: 'Fraction'):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other: 'Fraction'):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction'):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator,
                       self.denominator * other.denominator)

    def __truediv__(self, other: 'Fraction'):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Ділення на нульовий дріб")
        return Fraction(self.numerator * other.denominator,
                       self.denominator * other.numerator)

    if __name__ == "__main__":
        x = Fraction(1, 2)
        y = Fraction(1, 4)
        x + y == Fraction(3, 4)
