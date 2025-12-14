# Task_1
import requests
import json
from datetime import datetime

subreddit = "python"  # Оберіть свій сабреддіт
limit = 1000          # Максимум за один запит ~1000
before = None         # Для пагінації

all_comments = []

while True:
    url = "https://api.pushshift.io/reddit/comment/search/"
    params = {
        "subreddit": subreddit,
        "size": 500,
        "sort": "asc",
        "sort_type": "created_utc"
    }
    if before:
        params["before"] = before

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Помилка API")
        break

    data = response.json()
    comments = data["data"]
    if not comments:
        break

    all_comments.extend(comments)
    before = comments[-1]["created_utc"]
    print(f"Завантажено {len(comments)} коментарів, всього: {len(all_comments)}")

# Сортування за часом (на всяк випадок)
all_comments.sort(key=lambda x: x["created_utc"])

# Збереження у файл
with open(f"{subreddit}_comments.json", "w", encoding="utf-8") as f:
    json.dump(all_comments, f, indent=2, ensure_ascii=False)

print(f"Збережено {len(all_comments)} коментарів у {subreddit}_comments.json")

# Task_3

import sys

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t+%c+%C+%h+%w"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Погода в {city}: {response.text.strip()}")
    else:
        print("Помилка запиту")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python weather.py \"Місто\"")
    else:
        city = sys.argv[1]
        get_weather(city)
