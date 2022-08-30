# -*- coding: utf-8 -*-

# Задача на бинарный поиск с количества запросов
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=37&id_problem=212

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')
count = 0
for line in input_file:
    n = int(line)
    while n > 1:
        n = (n + 1) // 2  # количество запросов уменьшается в два раза c округлением вверх
        count += 1

    output_file.write(str(count))
