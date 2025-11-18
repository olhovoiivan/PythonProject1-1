# Task_1_Binary
def binary_search_recursive(arr, target, low, high):
    # Діапазон порожній (елемент не знайдено)
    if low > high:
        return -1
    # Знаходимо середній індекс
    mid = (low + high)
    # Елемент знайдено
    if arr[mid] == target:
        return mid
    # Якщо цільове значення менше, шукаємо у лівій половині
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    # Якщо цільове значення більше, шукаємо у правій половині
    else:  # target > arr[mid]
        return binary_search_recursive(arr, target, mid + 1, high)
sorted_list = [2, 5, 8, 12, 16, 25, 38, 42, 56, 64, 72, 88, 91]
target_value = int(input('Вкажіть будь-яке число та дізнайся його індекс: '))
n = len(sorted_list)
result = binary_search_recursive(sorted_list, target_value, 0, n - 1)
print(f"Список: {sorted_list}")
print(f"Пошук {target_value}: Індекс {result}")

# Task_2_Fibonacci_vid_AI
def fibonacci_search(arr, target):
    n = len(arr)
    # Знаходимо найменше число Фібоначчі Fk >= n
    # f_m_2 = F(k-2), f_m_1 = F(k-1), f_m = F(k)
    f_m_2 = 0  # F(0)
    f_m_1 = 1  # F(1)
    f_m = f_m_1 + f_m_2  # F(2)
    while f_m < n:
        f_m_2 = f_m_1
        f_m_1 = f_m
        f_m = f_m_1 + f_m_2
    # Зсув (offset) для відстеження початкового індексу
    offset = -1
    # f_m - це Fk
    # f_m_2 - це F(k-2)
    # f_m_1 - це F(k-1)
    while f_m > 1:
        # Визначаємо індекс для порівняння: min(offset + F(k-2), n-1)
        i = min(offset + f_m_2, n - 1)
        # Якщо елемент на індексі i менший за цільове
        if arr[i] < target:
            # Відкидаємо ліву частину до i, залишаємо F(k-1)
            f_m = f_m_1  # Новий Fk стає F(k-1)
            f_m_1 = f_m_2  # Новий F(k-1) стає F(k-2)
            f_m_2 = f_m - f_m_1  # Новий F(k-2) стає F(k-3)
            offset = i  # Зсуваємо початковий індекс
        # Якщо елемент на індексі i більший за цільове
        elif arr[i] > target:
            # Відкидаємо праву частину, залишаємо F(k-2)
            f_m = f_m_2  # Новий Fk стає F(k-2)
            f_m_1 = f_m_1 - f_m_2  # Новий F(k-1) стає F(k-3)
            f_m_2 = f_m - f_m_1  # Новий F(k-2) стає F(k-4)
        # Елемент знайдено
        else:
            return i
    # Спеціальна перевірка для F(1) (коли f_m_1 = 1)
    if f_m_1 == 1 and arr[offset + 1] == target:
        return offset + 1
    # Елемент не знайдено
    return -1

sorted_list = [2, 5, 8, 12, 16, 25, 38, 42, 56, 64, 72, 88, 91]
target_value = 5
result = fibonacci_search(sorted_list, target_value)

print(f"Список: {sorted_list}")
print(f"Пошук {target_value}: Індекс {result}")
