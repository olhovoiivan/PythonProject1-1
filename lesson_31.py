import os

# --- Конфігурація ---
SQL_FILE_NAME = 'task1.sql'

# --- SQL-КОМАНДИ (Вміст файлу task1.sql) ---
# Це багаторядковий рядок (multiline string)
sql_content = """
--
-- Завдання 1: Приєднання (JOINs)
-- Адаптація під навчальний проект "Фарма-сенс"
-- Використовується структура бази даних hr.db
--

-- Завдання 1: Відобразити ім'я, прізвище, номер відділу та назву відділу для кожного співробітника (INNER JOIN)
SELECT
    e.first_name AS "Ім'я",
    e.last_name AS "Прізвище",
    e.department_id AS "Номер Відділу",
    d.department_name AS "Назва Відділу"
FROM
    employees e
INNER JOIN
    departments d ON e.department_id = d.department_id;


-- Завдання 2: Відобразити ім'я та прізвище, відділ, місто та штат/область для кожного співробітника (Множинний JOIN)
SELECT
    e.first_name AS "Ім'я",
    e.last_name AS "Прізвище",
    d.department_name AS "Назва Відділу",
    l.city AS "Місто",
    l.state_province AS "Штат/Область"
FROM
    employees e
INNER JOIN
    departments d ON e.department_id = d.department_id
INNER JOIN
    locations l ON d.location_id = l.location_id;


-- Завдання 3: Відобразити ім'я, прізвище, номер відділу та назву відділу для всіх співробітників відділів 80 або 40
SELECT
    e.first_name AS "Ім'я",
    e.last_name AS "Прізвище",
    e.department_id AS "Номер Відділу",
    d.department_name AS "Назва Відділу"
FROM
    employees e
INNER JOIN
    departments d ON e.department_id = d.department_id
WHERE
    e.department_id IN (80, 40);


-- Завдання 4: Відобразити всі відділи, включаючи ті, де немає жодного співробітника (LEFT JOIN)
SELECT
    d.department_name AS "Назва Відділу",
    e.first_name AS "Ім'я Співробітника"
FROM
    departments d
LEFT JOIN
    employees e ON d.department_id = e.department_id
ORDER BY
    d.department_name;


-- Завдання 5: Вивести імена всіх співробітників, включаючи ім'я їхнього керівника (SELF JOIN)
SELECT
    e.first_name || ' ' || e.last_name AS "Співробітник",
    m.first_name || ' ' || m.last_name AS "Керівник"
FROM
    employees e
LEFT JOIN
    employees m ON e.manager_id = m.employee_id;

-- Завдання 6: Вивести посаду, повне ім'я та різницю між максимальною зарплатою для посади та зарплатою працівника (JOIN + Агрегація)
SELECT
    j.job_title AS "Посада",
    e.first_name || ' ' || e.last_name AS "Повне Ім'я",
    j.max_salary - e.salary AS "Різниця з Макс. Зарплатою"
FROM
    employees e
INNER JOIN
    jobs j ON e.job_id = j.job_id;

-- Завдання 7: Відобразити посаду та середню зарплату співробітників (GROUP BY + Агрегація)
SELECT
    j.job_title AS "Посада",
    printf("%.2f", AVG(e.salary)) AS "Середня Зарплата"
FROM
    employees e
INNER JOIN
    jobs j ON e.job_id = j.job_id
GROUP BY
    j.job_title
ORDER BY
    "Середня Зарплата" DESC;

-- Завдання 8: Відобразити повне ім'я та зарплату тих співробітників, які працюють у будь-якому відділі, розташованому в Лондоні
SELECT
    e.first_name || ' ' || e.last_name AS "Повне Ім'я",
    e.salary AS "Зарплата"
FROM
    employees e
INNER JOIN
    departments d ON e.department_id = d.department_id
INNER JOIN
    locations l ON d.location_id = l.location_id
WHERE
    l.city = 'London';

-- Завдання 9: Відобразити назву відділу та кількість співробітників у кожному відділі (LEFT JOIN + COUNT + GROUP BY)
SELECT
    d.department_name AS "Назва Відділу",
    COUNT(e.employee_id) AS "Кількість Співробітників"
FROM
    departments d
LEFT JOIN
    employees e ON d.department_id = e.department_id
GROUP BY
    d.department_name
ORDER BY
    "Кількість Співробітників" DESC;
"""
# --- Функція для створення файлу ---
def generate_sql_file(filename, content):
    """Створює файл і записує в нього SQL-контент."""
    try:
        # Відкриття файлу в режимі запису ('w') з кодуванням UTF-8
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content.strip()) # strip() видаляє зайві пробіли/переноси на початку/кінці
        print(f"Успішно створено файл: {filename}")
        print(f"Файл містить {len(content.splitlines())} рядків SQL-команд.")
    except IOError as e:
        print(f"Помилка при записі файлу {filename}: {e}")

# --- Виконання ---
if __name__ == "__main__":
    generate_sql_file(SQL_FILE_NAME, sql_content)
