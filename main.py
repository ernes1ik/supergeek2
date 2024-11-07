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
	{"Free Bird": 9.08, "Enter Sandman": 5.31, "One" : 7.45, "Sliver" : 2.10, "Come as You Are": 3.45},
	{"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong" : 4.51, "My Hero" : 4.02},
)

import random
from datetime import timedelta


def get_duration(playlist, n):
    def get_duration_from_string(s):
        name, duration_str = s.strip().split('\t')
        duration = timedelta(seconds=int(duration_str.split('.')[0]))
        return name, duration

    def get_duration_from_tuples(tuples):
        total_duration = timedelta()
        for song, duration in tuples:
            total_duration += duration
        return total_duration

    if isinstance(playlist, str):
        playlist = [get_duration_from_string(line) for line in playlist.split('\n')]
    elif isinstance(playlist, (list, tuple)):
        return get_duration_from_tuples(playlist)
    else:
        raise ValueError("Invalid playlist format")

    selected_songs = random.sample(playlist, n)
    total_duration = timedelta()
    for song, duration in selected_songs:
        total_duration += duration
    return total_duration