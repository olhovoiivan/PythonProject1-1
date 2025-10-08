def count_lines(name):
    """Підраховує кількість рядків у файлі."""
    with open(name, 'r', encoding='utf-8') as file:
        return len(file.readlines())

def count_chars(name):
    """Підраховує кількість символів у файлі."""
    with open(name, 'r', encoding='utf-8') as file:
        return len(file.read())

def test(name):
    """Викликає функції count_lines і count_chars для заданого файлу."""
    lines = count_lines(name)
    chars = count_chars(name)
    return lines, chars