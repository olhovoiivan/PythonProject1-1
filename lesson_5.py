#Task_1
import random
secret_num = random.randint(1, 10)
guess = int(input("Спробуй вгадати число від 1 до 10: "))
if guess == secret_num:
    print("Вітаємо! Ви вгадали число!")
else:
    print(f"На жаль, правильне число було {secret_num}.")
#Task_2
name = input("Введіть ваше ім’я: ")
age = int(input("Введіть ваш вік: "))
print(f"Привіт, {name}, на ваш наступний день народження вам буде {age + 1} років")
#Task_3
import random
input_str = input("Введіть рядок: ")
for i in range(5):
    random_word = ''.join(random.sample(input_str, len(input_str)))
    print(random_word)
