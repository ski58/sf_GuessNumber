"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_search_predict(number: int = 1) -> int:
    """Для угадывания числа используется метод половинного деления
        исследуемого интервала

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    lim_down = 0
    lim_up = 101
    count = 0

    while True:
        count += 1
        i_cur = (lim_up + lim_down) // 2 # находим середину исследуемого интервала
        if i_cur == number:
            break  # выход из цикла если угадали
        if number > i_cur:
            lim_down = i_cur # поднимаем нижнюю границу исследуемого интервала
        else :
            lim_up = i_cur # опускаем верхнюю  границу исследуемого интервала
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search_pred([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search_predict)
