import math
import time
import json
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
#  Task_1
CHISLA = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(5, sqrt_n, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_primes(numbers):
    """Послідовна фільтрація."""
    return [num for num in numbers if is_prime(num)]

def filter_primes_thread(numbers, max_workers=8):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, prime in zip(numbers, results) if prime]

def filter_primes_process(numbers, max_workers=8):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, prime in zip(numbers, results) if prime]

# Тестування та порівняння продуктивності
if __name__ == "__main__":
    print("Перевірка простих чисел")

    start = time.perf_counter()
    seq_primes = filter_primes(CHISLA)
    seq_time = time.perf_counter() - start

    start = time.perf_counter()
    thread_primes = filter_primes_thread(CHISLA)
    thread_time = time.perf_counter() - start

    start = time.perf_counter()
    process_primes = filter_primes_process(CHISLA)
    process_time = time.perf_counter() - start

    print("Результати однакові:", seq_primes == thread_primes == process_primes)
    print(f"Прості числа: {seq_primes}")
    print(f"Час послідовно:     {seq_time:.4f} с")
    print(f"Час ThreadPool:     {thread_time:.4f} с")
    print(f"Час ProcessPool:    {process_time:.4f} с")

# Task_2
    print("\n Завантаження коментарів з 'python' ===")
    SUBREDDIT = "python"
    MAX_PAGES = 10  # Обмеження для тесту (кожна сторінка ~500 коментарів)
    SIZE = 500  # Максимум на запит

    def fetch_page(before=None):
        url = "https://jsonplaceholder.typicode.com / comments?postId = {i}/"
        params = {
            "subreddit": SUBREDDIT,
            "size": SIZE,
            "sort": "desc",
            "sort_type": "created_utc",
        }
        if before:
            params["before"] = before

        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code != 200:
                return None, None
            data = response.json()["data"]
            new_before = data[-1]["created_utc"] if data else None
            return data, new_before
        except Exception as e:
            print(f"Помилка запиту: {e}")
            return None, None

    def download_sequential():
        """Послідовне завантаження."""
        comments = []
        before = None
        for _ in range(MAX_PAGES):
            page, before = fetch_page(before)
            if not page:
                break
            comments.extend(page)
            time.sleep(1.1)  # Rate limit
        return comments

    def download_thread_parallel():
        """Паралельне завантаження кількох сторінок одночасно (ThreadPool)."""
        futures = []
        befores = [None] * MAX_PAGES
        with ThreadPoolExecutor(max_workers=10) as executor:
            for b in befores:
                futures.append(executor.submit(fetch_page, b))
            comments = []
            for future in as_completed(futures):
                page, _ = future.result()
                if page:
                    comments.extend(page)
        return comments

    all_comments = download_thread_parallel()

    if all_comments:
        all_comments.sort(key=lambda c: c["created_utc"])

        print(f"Завантажено {len(all_comments)} коментарів")

        # Збереження в JSON
        with open("reddit_comments.json", "w", encoding="utf-8") as f:
            json.dump(all_comments, f, ensure_ascii=False, indent=2)

        print("Збережено у файл 'reddit_comments.json'")
    else:
        print("Не вдалося завантажити коментарі ")
