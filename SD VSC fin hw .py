import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # переменная для количества попыток
    count = 0
    # предполагаемое число
    predict = np.random.randint(1, 101)
    # задаем границы для бинарного поиска
    min_num = 0
    max_num= 100
    while True:
        count += 1
        # среднее значение заданных границ
        middle = (min_num + max_num) // 2
        # сравнение среднего значения с загаданным числом для сужения границ поиска
        if middle < number:
            low = middle + 1
        elif middle > number:
            high = middle - 1
        else:
            return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array: # запускаем функцию
        count_ls.append(game_core_v3(number)) 

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
