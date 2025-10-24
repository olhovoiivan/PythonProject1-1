# Task_1
class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'«Привіт, мене звати {self.firstname} {self.lastname}, мені {self.age} роки»')

person_1 = Person('Іван', 'Ольховой', 44)
person_1.talk()

# Task_2
class Dog():
    age_factor = 7
    def __init__(self, dog_ade):
        self.dog_ade = int(dog_ade)

    def human_age(self):
        return self.dog_ade * Dog.age_factor

dog1 = Dog(3)
print(dog1.human_age())

# Task_3
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels  # список каналів
        self.current_index = 0  # за замовчуванням — перший канал (індекс 0)

    def first_channel(self):
        """Увімкнути перший канал"""
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        """Увімкнути останній канал"""
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, n):
        """Увімкнути канал № n (нумерація з 1)"""
        if 1 <= n <= len(self.channels):
            self.current_index = n - 1
            return self.channels[self.current_index]
        else:
            return "Невірний номер каналу"

    def next_channel(self):
        """Увімкнути наступний канал (якщо останній — повернутись на перший)"""
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        """Увімкнути попередній канал (якщо перший — перейти на останній)"""
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        """Повернути назву поточного каналу"""
        return self.channels[self.current_index]

    def exists(self, name_or_number):
        """Перевірити, чи існує канал за номером або назвою"""
        if isinstance(name_or_number, int):
            return "Yes" if 1 <= name_or_number <= len(self.channels) else "No"
        elif isinstance(name_or_number, str):
            return "Yes" if name_or_number in self.channels else "No"
        else:
            return "No"
controller = TVController(CHANNELS)
print(f"Поточний канал: {controller.current_channel()}")
