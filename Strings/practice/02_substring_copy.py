# -*- coding: utf-8 -*-

# Задача на на поиск подстроки в строке
# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=42&id_problem=262


def string_equals(string, substring, i):
    return substring == string[i: i + len(substring)]


def substring_search(string, substring):
    result = []
    for i in range(len(string) - len(substring) + 1):
        if string_equals(string, substring, i):
            result.append(i)
    return result


text = input('Введите строку:\n')
 # строка
sub = input('Введите образ:\n')  # подстрока

# Количество вхождений подстроки в строке методом прямого поиска
sub_index = substring_search(text, sub)

# Делаем строку
answer = ' '.join(list(map(str, sub_index)))
print(answer)
