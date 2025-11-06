# Task_1
import logging
import os
import sys
import unittest

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContextFileManager:
    def __init__(self, filename, mode='r', encoding=None):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
        self.open_count = 0  # Лічильник відкриттів
        self.line_count = 0  # Лічильник рядків (для прикладу розширення)

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            self.open_count += 1
            logger.info(f"Файл '{self.filename}' відкрито в режимі '{self.mode}'. Відкриттів: {self.open_count}")

            if 'r' in self.mode:
                self.line_count = sum(1 for _ in self.file)
                self.file.seek(0)  # Повернутися на початок
                logger.info(f"Кількість рядків у файлі: {self.line_count}")

            return self.file
        except Exception as e:
            logger.error(f"Помилка при відкритті файлу '{self.filename}': {e}")
            raise
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            logger.info(f"Файл '{self.filename}' закрито. Відкриттів: {self.open_count}")
        if exc_type is not None:
            logger.error(f"Виняток у контексті: {exc_type.__name__}: {exc_value}")
            return False

# Task_2
class TestContextFileManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'test_file.txt'
        with open(self.test_filename, 'w') as f:
            f.write("Рядок 1\nРядок 2\nРядок 3\n")

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_positive_open_read(self):
        """тест: відкриття для читання"""
        with ContextFileManager(self.test_filename, 'r') as f:
            content = f.read()
            self.assertEqual(content, "Рядок 1\nРядок 2\nРядок 3\n")

    def test_positive_open_write(self):
        """тест: відкриття для запису"""
        with ContextFileManager(self.test_filename, 'w') as f:
            f.write("Новий контент")
        with open(self.test_filename, 'r') as f:
            self.assertEqual(f.read(), "Новий контент")

    def test_line_count(self):
        """Тест лічильника рядків"""
        manager = ContextFileManager(self.test_filename, 'r')
        with manager as f:
            self.assertEqual(manager.line_count, 3)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

# Task_3
import pytest
def process_text(file_obj):
    content = file_obj.read()
    words = content.split()
    return len(words)

@pytest.fixture
def file_fixture():
    """Фікстура, яка використовує менеджер контексту"""
    filename = 'pytest_test_file.txt'
    with open(filename, 'w') as f:
        f.write("Це тестовий файл з кількома словами.")
    try:
        with ContextFileManager(filename, 'r') as file_obj:
            yield file_obj
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def test_process_text(file_fixture):
    word_count = process_text(file_fixture)
    assert word_count == 6  

def run_pytest():
    original_stdout = sys.stdout
    pytest.main(['-v', '--tb=short'])
    output = sys.stdout.getvalue()
    sys.stdout = original_stdout
    return output

print("\nРезультати pytest для Завдання 3:")
print(run_pytest())
