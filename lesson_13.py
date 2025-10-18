# Task_1
def func_local_variables(func):
    """Повертає кількість локальних змінних у заданій функції."""
    return func.__code__.co_nlocals
def func_local():
    x = 10
    y = 5
    z = x + y
    return z
print(f"Кількість локальних змінних у функції: {func_local_variables(func_local)}")
# Task_2
def func_one():
    def func_two():
        return "Це виклик внутрішньої функції!"
    return func_two  # Повертаємо внутрішню функцію
func_3 = func_one()  # Отримуємо внутрішню функцію
print(func_3())
# Task_3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    return func2(nums)
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
print(choose_func(nums1, square_nums, remove_negatives))  # [1, 4, 9, 16, 25]
print(choose_func(nums2, square_nums, remove_negatives))  # [1, 3, 5]
