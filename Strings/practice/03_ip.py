# -*- coding: utf-8 -*-

# Задача на проверку строки
# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=41&id_problem=269

input_file = open('input.txt', 'r', encoding='utf8')
output_file = open('output.txt', 'w', encoding='utf8')

# ip = input_file.read()
ip = '88.144.996.11'
list_ip = ip.split('.')

answer = ' '.join(list(map(str, list_ip)))
bad = 0

for mask in list_ip:
    if 0 < int(mask) > 255:
        bad += 1
        if bad > 0:
            output_file.write('Bad')
        else:
            output_file.write('Good')
