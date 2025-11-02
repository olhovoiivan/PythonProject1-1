# Task_1

class UserEmail:
    def __init__(self, email: str):
        self.email = self.validate(email)

    def validate(self, email: str):
        if not isinstance(email, str):
            raise ValueError("Електронна пошта має бути рядком.")

        if '@' not in email:
            raise ValueError("Електронна пошта повинна містити символ '@'.")

        if email.count('@') > 1:
            raise ValueError("Електронна пошта може містити лише один символ '@'.")

        local_part, domain_part = email.rsplit('@', 1)

        if not local_part or not domain_part:
            raise ValueError("Локальна або доменна частина порожні.")

        if '.' not in domain_part:
            raise ValueError("Домен повинен містити крапку.")

        if domain_part.startswith('.') or domain_part.endswith('.'):
            raise ValueError("Домен не може починатися або закінчуватися крапкою.")

        if '..' in domain_part:
            raise ValueError("Домен не може містити дві крапки поспіль.")

        return email

try:
    user1 = UserEmail("testtwo@example.com")
    print(f"Створено користувача: {user1.email}")

except ValueError as e:
    print(f"Помилка: {e}")

try:
    user2 = UserEmail("testtwo@@@example.com")
    print(f"Створено користувача: {user2.email}")

except ValueError as e:
    print(f"Помилка: {e}")

# Task_2

class Boss():
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def get_workers(self):
        return self.workers

    def set_workers(self, new_list):
        raise AttributeError("Не можна напряму присвоїти список працівників.")

    def add_worker(self, worker_id: int):
        if worker_id not in self.workers:
            self.workers.append(worker_id)
            print(f"Boss {self.name} додав працівника з ID {worker_id}.")
        else:
            print(f"Працівник з ID {worker_id} вже є у списку {self.name}.")

class Worker:
    def __init__(self, id_: int, name: str, company: str, initial_boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None   # ШІ
        self.set_boss(initial_boss)  # Викликаємо сетер для первинної валідації ШІ

    def get_boss(self):  # getter Boss
        return self._boss

    def set_boss(self, new_boss):  # setter Boss
        if not isinstance(new_boss, Boss):
            raise TypeError("Значення boss має бути екземпляром класу Boss.")
        if self._boss:
            new_boss.add_worker(self.id)
            self._boss = new_boss
            print(f"ІНФО: Працівнику {self.name} призначено нового боса: {new_boss.name}")


