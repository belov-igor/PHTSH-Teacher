# -*- coding: utf-8 -*-

# Задача на на поиск подстроки в строке
# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=41&id_problem=270


def string_equals(text, substring, i):
    return substring == text[i: i + len(substring)]


def substring_search(text, substring):
    result = []
    for i in range(len(text) - len(substring)):
        if string_equals(text, substring, i):
            result.append(i)
    return result


input_file = open('input.txt', 'r', encoding='utf8')
output_file = open('output.txt', 'w', encoding='utf8')

arrows = input_file.read()
sub_1 = ">>-->"  # подстрока
sub_2 = "<--<<"

# Количество вхождений подстроки в строке методом прямого поиска
arrows_count_1 = len(substring_search(arrows, sub_1))
arrows_count_2 = len(substring_search(arrows, sub_2))
arrows_count = arrows_count_1 + arrows_count_2

# Запись в файл
output_file.write(str(arrows_count))

input_file.close()
output_file.close()
