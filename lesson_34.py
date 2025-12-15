# Task_1
from threading import Thread

counter = 0      # глобальний спільний лічильник
rounds = 100_000 # кількість ітерацій на один потік

class Counter(Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            counter += 1  # інкремент лічильника

# Створення та запуск двох потоків
t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Фінальне значення лічильника: {counter}")

from threading import Thread, Lock

counter = 0
rounds = 100_000
lock = Lock()  # об’єкт блокування

class Counter(Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with lock:        # критична секція
                counter += 1

# Запуск
t1 = Counter()
t2 = Counter()
t1.start()
t2.start()
t1.join()
t2.join()

print(f"Фінальне значення лічильника: {counter}")  # завжди 200000

# Task_2
import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 12345        # довільний порт > 1024

def handle_client(conn: socket.socket, addr):
    """Обробляє одного клієнта в окремому потоці"""
    print(f"Підключено клієнта: {addr}")
    try:
        while True:
            data = conn.recv(1024)  # отримуємо до 1024 байт
            if not data:            # клієнт закрив з’єднання
                break
            print(f"Отримано від {addr}: {data.decode('utf-8').strip()}")
            conn.sendall(data)      # відправляємо ті самі дані назад (echo)
    except Exception as e:
        print(f"Помилка при роботі з {addr}: {e}")
    finally:
        print(f"Відключено клієнта: {addr}")
        conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Сервер слухає {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server.accept()              # чекаємо клієнта
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True                      # потік завершиться при виході головного
            thread.start()
    except KeyboardInterrupt:
        print("\nСервер зупинено.")
    finally:
        server.close()

if __name__ == "__main__":
    main()
