#Task_1
import random
random_num  = []
count = 0
while count < 10:
    random_num.append(random.randint (1, 20))
    count += 1
print(f"Згенрованний список чисел : {random_num}")
largest_num = random_num[0]
index = 1
while index < len(random_num):
    if random_num[index] > largest_num:
        largest_num = random_num[index]
    index +=  1
print(f"Найбільше число у списку: {largest_num}")
#Task_2
list_random_1 = []
list_random_2 = []
count = 0
while count < 10:
    list_random_1.append(random.randint(1,10))
    list_random_2.append(random.randint(1,10))
    count += 1
print(f"Згенерований 1 список чисел: {list_random_1}")
print(f"Згенерований 2 список чисел: {list_random_2}")
common_num = []
index1 = 0
while index1 < len(list_random_1):
    current_num = list_random_1[index1]
    found_in_list2 = False
    index2 = 0
    while index2 < len(list_random_2):
        if list_random_2[index2] == current_num:
            found_in_list2 = True
            break
        index2 += 1
    if found_in_list2:
        already_in_common = False
        index_common = 0
        while index_common < len(common_num):
            if common_num[index_common] == current_num:
                already_in_common = True
                break
            index_common += 1
        if not already_in_common:
            common_num.append(current_num)
    index1 += 1
print(f"Спільні числа без дублікатів: {common_num}")
#Task_3
def extract_numbers():
    numbers = []
    num = 1
    while num <= 100:
        numbers.append(num)
        num += 1
    result_7 = []
    index = 0
    while index < len(numbers):
        if numbers[index] % 7 == 0 and numbers[index] % 5 != 0:
            result_7.append(numbers[index])
        index += 1
    return result_7
result = extract_numbers()
print(f"Числа, що діляться на 7, але не діляться на 5: {result}")