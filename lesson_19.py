# Task_1
def with_index(iterable, start=0):
    i = start
    for item in iterable:
        yield i, item
        i += 1
data = ['a', 'b', 'c']

# Тест 1: З start=0
result_default = list(with_index(data))
# Очікується: [(0, 'a'), (1, 'b'), (2, 'c')]
print(f"Результат (start=0): {result_default}")

# Тест 2: З start=10
result_custom = list(with_index(data, start=10))
# Очікується: [(10, 'a'), (11, 'b'), (12, 'c')]
print(f"Результат (start=10): {result_custom}")

# Task_2
def in_range(start, end=None, step=1):

    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError("step не може бути 0")
    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step

print(list(in_range(5)))
print(list(in_range(2, 7, 2)))
print(list(in_range(10, 0, -2)))
print(list(in_range(3, 3)))

# Task_3
class MySequence:

   def __init__(self, *items):
        self._data = list(items)

   def __iter__(self):
       self._index = 0
       return self

   def __next__(self):
       if self._index >= len(self._data):
           raise StopIteration

       value = self._data[self._index]
       self._index += 1
       return value

   def __getitem__(self, idx):
        return self._data[idx]

   def __len__(self):
        return len(self._data)

   def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(map(repr, self._data))})"

if __name__ == "__main__":
   
    print("\nMySequence:")
    seq = MySequence(10, 20, 30, 40)
    print("len(seq) =", len(seq))
    print("seq[2] =", seq[2])
    print("seq[1:3] =", seq[1:3])

    for x in seq:
        print("->", x)

    print("\nПовторна ітерація:")
    for x in seq:
        print("->", x)
