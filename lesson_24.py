# Task_1
class Stak():
    def __init__(self):
        self._items =[]

    def is_empty(self):
        return not self._items

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек порожній. Неможливо виконати pop.")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек порожній. Неможливо виконати peek.")
        return self._items[-1]

    def size(self):
        return len(self._items)

def reverse_sequence():
    input_sequence = input("Введіть слово: ")
    w_stack = Stak()
    print(f"\n1. Завантаження символів у стек: {input_sequence}")
        # КРОК 1: Завантажуємо символи у стек (LIFO)
    for char in input_sequence:
        w_stack.push(char)
        print(f"   -> Додано '{char}'. Розмір стеку: {w_stack.size()}")
        print("\n2. Виведення символів у зворотному порядку (витягуємо з вершини):")
        reversed_sequence = ""
        # КРОК 2: Витягуємо символи зі стеку, вони виходять у зворотному порядку
    while not w_stack.is_empty():
        char = w_stack.pop()
        reversed_sequence += char
        print(f"   <- Витягнуто '{char}'. Залишилося: {w_stack.size()}")

        print("-" * 30)
        print(f"Початкова послідовність: {input_sequence}")
        print(f"Обернена послідовність: {reversed_sequence}")
        print("-" * 30)

    # Виконання програми
if __name__ == "__main__":
    reverse_sequence()

# TasK_2

class Stack:
    def __init__(self):
        self._items = []
    def is_empty(self):
        return not self._items
    def push(self, item):
        self._items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек порожній")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек порожній")
        return self._items[-1]
def is_balanced(sequence):
    s = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}
    openers = set(brackets_map.values())
    for char in sequence:
        # 1. Якщо символ - відкриваюча дужка, додаємо її у стек
        if char in openers:
            s.push(char)
        # 2. Якщо символ - закриваюча дужка
        elif char in brackets_map:
            # Перевірка 1: Стек порожній (немає відповідної відкритої дужки)
            if s.is_empty():
                print(f"   -> Незбалансовано: Знайдено закриваючу '{char}', але стек порожній.")
                return False
            # Витягуємо останню відкриваючу дужку
            last_opener = s.pop()
            # Перевірка 2: Невідповідність (відкриваюча дужка не збігається з потрібною)
            if last_opener != brackets_map[char]:
                print(f"   -> Незбалансовано: Очікували '{brackets_map[char]}', але знайшли '{last_opener}'.")
                return False
        # 3. Перевірка після проходження всієї послідовності
        # Якщо стек порожній, усі відкриваючі дужки були закриті
    return s.is_empty()
test_cases = ["()", "{)", "{]", "{{}}"]

for exp in test_cases:
    result = is_balanced(exp)
    print(f"Послідовність: '{exp}' -> Результат: {'ЗБАЛАНСОВАНО' if result else 'НЕЗБАЛАНСОВАНО'}\n"
          
# Task_3
class Queue():
    def __init__(self):
        self._items = []
    def is_empty(self):
        return not self._items
    def enqueue(self, item): 
        self._items.append(item)
    def dequeue(self): 
        if self.is_empty():
            raise IndexError("Черга порожня. Неможливо виконати dequeue.")
        return self._items.pop(0)  # Вилучаємо перший елемент
    def size(self):
        return len(self._items)
    
    def get_from_queue(self, target_element):
        """
        Шукає та повертає target_element з черги.
        Порядок усіх інших елементів залишається незмінним.
        """
        temp_queue = Queue()
        found = False
        original_size = self.size()

        # Крок 1: Пошук елемента
        for _ in range(original_size):
            current_item = self.dequeue()
            if current_item == target_element:
                found = True
                # Знайдений елемент не додаємо нікуди, він вилучається
            else:
                # Всі інші елементи тимчасово переміщуємо у допоміжну чергу
                temp_queue.enqueue(current_item)
        # Крок 2: Обробка результату пошуку та відновлення черги
        if not found:
            # Якщо елемент не знайдено, переносимо всі елементи з temp_queue назад
            # Вони повертаються у початкову чергу в тому ж порядку
            while not temp_queue.is_empty():
                self.enqueue(temp_queue.dequeue())

            # Викликаємо виняток
            raise ValueError(f"Елемент '{target_element}' не знайдено у черзі.")
        # Крок 3: Відновлення порядку (якщо елемент знайдено)
        # Переміщуємо елементи з допоміжної черги назад в основну
        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())
        print(f"Елемент '{target_element}' успішно вилучено. Порядок збережено.")
        return target_element

# --- Тестування Queue ---
print("--- Тестування Queue.get_from_queue ---")
q = Queue()
[q.enqueue(x) for x in ['A', 'B', 'C', 'D', 'E']]  
print(f"Початкова черга (голова до хвоста): {q._items}")
