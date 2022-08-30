# -*- coding: utf-8 -*-


def ternary_search(seq, val):
    """
    Функция тернарного поиска
    :param seq: Отсортированная последовательность (список) целых чисел
    :param val: Искомое число
    :return: Индекс найденного числа, None - если число не найдено
    """
    left = 0
    right = len(seq) - 1
    while left <= right:
        step = (right - left) // 3
        mid1 = left + step
        mid2 = right - step
        if seq[mid1] == val:
            return mid1
        if seq[mid2] == val:
            return mid2
        if seq[mid1] < val < seq[mid2]:
            left = mid1 + 1
            right = mid2 - 1
        elif val < seq[mid1]:
            right = mid1 - 1
        else:
            left = mid2 + 1
    return None


# sequence = [-2, 0, 3, 5, 7, 9, 11, 15, 18]
# find = ternary_search(sequence, 11)
# print(find)
