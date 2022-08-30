# -*- coding: utf-8 -*-

# Задача на на поиск подстроки в строке
# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=41&id_problem=267

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

n = input_file.read()
zero_count = n.count('0')  # количество вхождений подстроки в строке (работает только с непересающимися подстроками)

output_file.write(str(zero_count))

input_file.close()
output_file.close()
