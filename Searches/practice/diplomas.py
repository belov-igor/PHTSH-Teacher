# -*- coding: utf-8 -*-

# Задача на бинарный поиск с подсчетом стороны доски для размещения дипломов
# https://acmp.ru/index.asp?main=task&id_task=712

def diplomas_number(width, height, length):
    """
    :param width: ширина диплома
    :param height: высота диплома
    :param length:
    :return:
    """
    return (length // height) * (length // width)


def find_answer(width, height, count):
    """
    :param width: ширина поля
    :param height: высота поля
    :param count: количество дипломов
    :return: минимальный размер стороны доски, которая нужна для размещения всех дипломов
    """
    left = 0
    right = max(width, height) * count
    while left + 1 < right:
        mid = (left + right) // 2
        if diplomas_number(height, width, mid) >= count:
            right = mid
        else:
            left = mid
    return right


# Открытие файлов
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

# Получение входных данных
input_data = input_file.read()
str_w, str_h, str_n = input_data.split()
w, h, n = int(str_w), int(str_h), int(str_n)

# Решение
ans = find_answer(w, h, n)

# Запись в выходной файл
output_file.write(str(ans))
