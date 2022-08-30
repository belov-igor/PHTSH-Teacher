# -*- coding: utf-8 -*-

# Задача на расчет префикс-функции
# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=42&id_problem=280

def prefix_function(string):
    n = len(string)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and string[j] != string[i]:
            j = pi[j-1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi


input_file = open('input.txt', 'r', encoding='utf8')
output_file = open('output.txt', 'w', encoding='utf8')

strings = input_file.readlines()

for string in strings:
    pi = prefix_function(string)

    # Делаем строку
    answer = ' '.join(list(map(str, pi)))
    output_file.write(f'{answer}\n')
