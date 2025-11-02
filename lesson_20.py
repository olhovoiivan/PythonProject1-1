# Task_1
import unittest
from lesson_16 import Mathematician

class TestFilterLeaps(unittest.TestCase):

    def setUp(self):
        """Ініціалізація об'єкта перед кожним тестом."""
        self.mathematician = Mathematician()

    def test_basic_mixed_years(self):
        """Тест зі змішаним списком, що містить високосні та не високосні роки."""
        years = [2001, 1884, 1995, 2003, 2020, 1981]
        expected = [1884, 2020]
        actual = self.mathematician.filter_leaps(years)
        self.assertEqual(actual, expected)

    def test_century_not_leap(self):
        """Тест, що перевіряє століття, які не є високосними (діляться на 100, але не на 400)."""
        years = [1700, 1800, 1900]
        expected = []
        actual = self.mathematician.filter_leaps(years)
        self.assertEqual(actual, expected)

    def test_century_is_leap(self):
        """Тест, що перевіряє століття, які є високосними (діляться на 400)."""
        years = [1600, 2000, 2400]
        expected = [1600, 2000, 2400]
        actual = self.mathematician.filter_leaps(years)
        self.assertEqual(actual, expected)

    def test_no_leap_years(self):
        """Тест списку, де немає жодного високосного року."""
        years = [2023, 2021, 1999, 1998]
        expected = []
        actual = self.mathematician.filter_leaps(years)
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """Тест на роботу з пустим вхідним списком."""
        years = []
        expected = []
        actual = self.mathematician.filter_leaps(years)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

# Task_2 Тести для validate_phone, які можуть бути застосовані до попередньої телефонної книги

    def test_validate_phone_valid(self):
        """Перевірка коректного номера."""
        self.assertTrue(validate_phone("0971234567"))

    def test_validate_phone_too_short(self):
        """Перевірка номера менше 10 цифр."""
        self.assertFalse(validate_phone("123"))

    def test_validate_phone_with_letters(self):
        """Перевірка номера з нецифровими символами."""
        self.assertFalse(validate_phone("123456789a"))
