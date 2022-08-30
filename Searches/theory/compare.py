from random import randint, choice
from linear_search import linear_search
from binary_search import binary_search_iterative, binary_search_recursive
from ternary_search import ternary_search
import time


def generate_sequence(n):
    """
    :param n: количество элементов в последовательности
    :return: сортированная последовательность уникальных чисел от 1 до 1000
    """
    seq_unsort = []
    for i in range(n):
        seq_unsort.append(randint(1, 1000))
    seq_sort = sorted(seq_unsort)
    seq_set = set(seq_sort)
    uniq_seq = list(seq_set)
    return uniq_seq


# Сгенерируем последовательность побольше
big_sequence = generate_sequence(n=1000000)
print(big_sequence)

# Чуть помухлюем и возьмем число из последовательности
value = choice(big_sequence)
print(f'Ищем число - {value}')


# Линейный поиск
start = time.time()
line_search = linear_search(seq=big_sequence, val=value)
end = time.time()
print(f'Время выполнения линейного поиска {end - start}')

# Итеративный бинарный поиск
start = time.time()
bin_search_iter = binary_search_iterative(seq=big_sequence, val=value)
end = time.time()
print(f'Время выполнения итеративного бинарного поиска {end - start}')

# Рекурсивный бинарный поиск
start = time.time()
bin_search_r = binary_search_recursive(seq=big_sequence, val=value, left=0, right=len(big_sequence) - 1)
end = time.time()
print(f'Время выполнения рекурсивного бинарного поиска {end - start}')

# Тернарный поиск
start = time.time()
tern_search = ternary_search(seq=big_sequence, val=value)
end = time.time()
print(f'Время выполнения тернарного поиска {end - start}')
