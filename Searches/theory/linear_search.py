# -*- coding: utf-8 -*-

def linear_search(seq, val):
    """
    Функция линейного поиска
    :param seq: Отсортированная последовательность (список) целых чисел
    :param val: Искомое число
    :return: Индекс найденного числа, None - если число не найдено
    """
    for i in range(len(seq)):
        if seq[i] == val:
            return i
    return None


# sequence = [-2, 0, 3, 5, 7, 9, 11, 15, 18]
# find = linear_search(sequence, 11)
# print(find)
