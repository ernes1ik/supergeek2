## project_5
# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * многострочная строка
#   * кортеж из двух словарей
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""

playlist_f = (
    {"Free Bird": 9.08, "Enter Sandman": 5.31, "One": 7.45, "Sliver": 2.10, "Come as You Are": 3.45},
    {"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong": 4.51, "My Hero": 4.02},
)

import random
from datetime import timedelta
from typing import Iterable, Any, Union


def parse_playlist(playlist: str) -> list:
    songs = []
    for line in playlist.strip().split("\n"):
        name, duration = line.rsplit(" ", 1)
        songs.append((name, float(duration)))
    return songs


def get_duration(playlist: Iterable, n: int) -> Union[timedelta, str, float]:
    if isinstance(playlist, str):
        playlist = parse_playlist(playlist)
    elif isinstance(playlist, tuple) and all(isinstance(i, dict) for i in playlist):
        playlist = [(song['title'], song['duration']) for song in playlist]

    if n > len(playlist):
        return

    chosen_songs = random.sample(playlist, n)

    total_duration = sum(song[1] for song in chosen_songs)

    return timedelta(hours=int(total_duration // 60), minutes=int(total_duration % 60))


multi_line_playlist = """
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go 4.40
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""

dict_playlist = (
    {"title": "Why Does My Heart Feel so Bad?", "duration": 4.23},
    {"title": "Everlong", "duration": 3.25},
    {"title": "To Let Myself Go", "duration": 4.40},
    {"title": "Golden", "duration": 2.56},
    {"title": "Daisuke", "duration": 2.41},
    {"title": "Miami", "duration": 3.31},
    {"title": "Chill Bill Lofi", "duration": 2.05},
    {"title": "The Perfect Girl", "duration": 1.48},
    {"title": "Resonance", "duration": 3.32},
)

print(get_duration(multi_line_playlist, 3))
print(get_duration(dict_playlist, 3))
