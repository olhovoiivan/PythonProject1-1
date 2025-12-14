import socket

# UDP Сервер
# Налаштування
HOST = '127.0.0.1'  # localhost
PORT = 12345
# Створення UDP сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP сервер запущено на {HOST}:{PORT}")
print("Очікування повідомлень...")

while True:
    # Отримання даних (до 1024 байт) та адреси клієнта
    data, addr = server_socket.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"Отримано від {addr}: {message}")

    # Повернення echo
    server_socket.sendto(data, addr)
    print(f"Відправлено echo назад на {addr}")

# UDP Клієнт
# Налаштування
HOST = '127.0.0.1'
PORT = 12345

# Створення UDP сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP клієнт запущено. Введіть повідомлення (або 'exit' для виходу):")

while True:
    message = input("Ваше повідомлення: ")
    if message.lower() == 'exit':
        break

    # Відправка повідомлення
    client_socket.sendto(message.encode('utf-8'), (HOST, PORT))

    # Отримання відповіді
    data, server = client_socket.recvfrom(1024)
    response = data.decode('utf-8')
    print(f"Отримано від сервера: {response}")

client_socket.close()
