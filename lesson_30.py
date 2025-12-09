import os
import sqlite3

DB_NAME = 'pharmacy_data.db'
SQL_FILE = 'task30.sql'

# Якщо файл існує — видаляємо для чистого запуску
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

try:
    # Підключення до БД
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print(f"Підключено до бази даних: {DB_NAME}")

    # 1. Створення таблиці
    cursor.execute("""
        CREATE TABLE Medicine_Assortment (
            ProductID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Manufacturer TEXT,
            Price REAL,
            ExpiryDate DATE
        );
    """)
    print("-> Таблицю 'Medicine_Assortment' створено.")

    # 2. Перейменування таблиці
    cursor.execute("ALTER TABLE Medicine_Assortment RENAME TO PharmacyStock;")
    print("-> Таблицю перейменовано на 'PharmacyStock'.")

    # 3. Додавання нового стовпця
    cursor.execute("ALTER TABLE PharmacyStock ADD COLUMN Category TEXT;")
    print("-> Додано стовпець 'Category'.")

    # 4. Вставка даних
    products_to_insert = [
        (101, 'Парацетамол 500 мг', 'Фармак', 45.50, '2026-05-15', 'Знеболюючі'),
        (102, 'Вітамін С (шипучий)', 'Bayer', 120.00, '2025-11-01', 'Вітаміни'),
        (103, 'Антисептик-спрей', 'HealthGuard', 88.99, '2027-02-28', 'Перев’язувальні')
    ]

    cursor.executemany("""
        INSERT INTO PharmacyStock (ProductID, Name, Manufacturer, Price, ExpiryDate, Category)
        VALUES (?, ?, ?, ?, ?, ?)
    """, products_to_insert)
    print(f"-> Додано {cursor.rowcount} рядків.")

    # 5. Оновлення даних
    cursor.execute("""
        UPDATE PharmacyStock
        SET Price = 49.90, Category = 'Жарознижуючі'
        WHERE ProductID = 101;
    """)
    print(f"-> Оновлено {cursor.rowcount} рядок/рядків (ProductID 101).")

    # 6. Видалення по умові
    cursor.execute("""
        DELETE FROM PharmacyStock
        WHERE ProductID = 102 AND ExpiryDate < '2026-01-01';
    """)
    print(f"-> Видалено {cursor.rowcount} рядок/рядків (ProductID 102).")

    # 7. SELECT — перевірка результату
    cursor.execute("SELECT * FROM PharmacyStock;")
    rows = cursor.fetchall()

    print("\n--- Фінальний вміст 'PharmacyStock' ---")
    for row in rows:
        print(row)

    conn.commit()
    print("Усі зміни збережено.")

except sqlite3.Error as e:
    print(f"Помилка SQLite: {e}")

finally:
    if conn:
        conn.close()
        print("З'єднання з базою даних закрито.")

# Генерація SQL-файлу

sql_content = """
-- 1. Створення таблиці
CREATE TABLE Medicine_Assortment (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Manufacturer TEXT,
    Price REAL,
    ExpiryDate DATE
);

-- 2. Перейменування таблиці
ALTER TABLE Medicine_Assortment RENAME TO PharmacyStock;

-- 3. Додавання нового стовпця
ALTER TABLE PharmacyStock ADD COLUMN Category TEXT;

-- 4. Вставка рядків
INSERT INTO PharmacyStock VALUES
(101, 'Парацетамол 500 мг', 'Фармак', 45.50, '2026-05-15', 'Знеболюючі'),
(102, 'Вітамін С (шипучий)', 'Bayer', 120.00, '2025-11-01', 'Вітаміни'),
(103, 'Антисептик-спрей', 'HealthGuard', 88.99, '2027-02-28', 'Перев’язувальні');

-- 5. Оновлення рядка
UPDATE PharmacyStock
SET Price = 49.90, Category = 'Жарознижуючі'
WHERE ProductID = 101;

-- 6. Видалення рядка
DELETE FROM PharmacyStock
WHERE ProductID = 102 AND ExpiryDate < '2026-01-01';
"""

with open(SQL_FILE, "w", encoding="utf-8") as f:
    f.write(sql_content.strip())
