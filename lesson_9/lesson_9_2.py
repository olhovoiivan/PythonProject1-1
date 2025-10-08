# Task_1
import lesson_9_1
print(lesson_9_1.func_name('Іван'))
print(lesson_9_1.func_age(44))
# Task_2
import sys
print(sys.path)   # ['C:\\Users\\user\\PycharmProjects\\PythonProject02', 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2025.1.1.1\\plugins\\python-ce\\helpers\\pydev', 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2025.1.1.1\\plugins\\python-ce\\helpers\\third_party\\thriftpy', 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2025.1.1.1\\plugins\\python-ce\\helpers\\pydev', 'C:\\Users\\user\\PycharmProjects\\PythonProject02', 'C:\\Users\\user\\PycharmProjects\\PythonProject02\\.venv\\Scripts\\python313.zip', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\user\\PycharmProjects\\PythonProject02\\.venv',
# 'C:\\Users\\user\\PycharmProjects\\PythonProject02\\.venv\\Lib\\site-packages', 'C:\\Users\\user\\PycharmProjects\\PythonProject02']
print(len(sys.path))
'''
Так, sys.path — це звичайний список Python, який можна модифікувати, додаючи, 
видаляючи або змінюючи елементи. Зміни в sys.path впливають на те, де Python 
шукає модулі, але ці зміни діють лише під час поточного виконання програми 
і не впливають на змінну середовища PYTHONPATH або поведінку в інших сесіях.
'''
sys.path.insert(0, 'C:\\Users\\user\\Agent-007')
print(sys.path[0])
sys.path.append('THE_END')
print(sys.path[-1])
# Task_3
import mymod
print(mymod.count_lines('testfile.txt'))
print(mymod.count_chars('testfile.txt'))
print(mymod.test('testfile.txt'))