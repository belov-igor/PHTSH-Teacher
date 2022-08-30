# -*- coding: utf-8 -*-

def binary_search_iterative(seq, val):
    """
    Функция бинарного поиска
    :param seq: Отсортированная последовательность (список) целых чисел
    :param val: Искомое число
    :return: Индекс найденного числа, None - если число не найдено
    """
    first = 0
    last = len(seq) - 1
    mid = len(seq) // 2
    while seq[mid] != val and first <= last:
        if val > seq[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
    if first > last:
        return None
    else:
        return mid


def binary_search_recursive(seq, val, left, right):
    """
    Функция бинарного поиска с рекурсией
    :param left: Начало диапазона
    :param right: Конец диапазона
    :param seq: Отсортированная последовательность (список) целых чисел
    :param val: Искомое число
    :return: Индекс найденного числа, None - если число не найдено
    """
    if left > right:  # Условие выхода
        return None
    else:
        mid = (left + right) // 2
        if val == seq[mid]:
            return mid
        elif val < seq[mid]:
            return binary_search_recursive(seq, val, left, mid + 1)
        else:
            return binary_search_recursive(seq, val, mid + 1, right)


# sequence = [-2, 0, 3, 5, 7, 9, 11, 15, 18]
# find = binary_search_iterative(sequence, 11, 0, len(sequence) - 1)
# print(find)
