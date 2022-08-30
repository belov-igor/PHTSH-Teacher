# -*- coding: utf-8 -*-

# Задача на бинарный поиск
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=37&id_problem=1631


# Открытие файлов
input_file = open('practice/input.txt', 'r')
output_file = open('practice/output.txt', 'w')
lines = input_file.readlines()

# Получение входных данных
str_n, str_k, str_x, str_y = lines[0].split()
n, k, x, y = int(str_n), int(str_k), int(str_x), int(str_y)
nq = int(lines[1])

rooms_on_entrance = (n // k) * x + (n - n // k) * y  # комнат в подъезде
rooms_on_block = (k - 1) * y + x


for room in lines[2].split():
    room = int(room) - 1
    room %= rooms_on_entrance
    block = room // rooms_on_block
    room %= rooms_on_block
    floor = room // y
    if floor > k - 1:
        floor = k - 1
    output_file.write(f'{block * k + floor + 1}\n')
