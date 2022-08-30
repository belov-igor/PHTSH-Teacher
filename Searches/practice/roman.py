# -*- coding: utf-8 -*-

# Задача на бинарный поиск с подсчетом максимального количества глав в томе
# https://acmp.ru/index.asp?main=task&id_task=523

# Открытие файлов
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

# Получение входных данных
lines = input_file.readlines()
n = int(lines[0])  # количество глав

list_pages_count = []
list_pages_count_str = lines[1].split()
for page_str in list_pages_count_str:
    page = int(page_str)
    list_pages_count.append(page)    # количество страниц в главе

k = n = int(lines[2])  # количество томов

# Двоичный поиск
left = 0
right = 32767
while left + 1 < right:
    mid = left + right // 2
    volumes_count = 0
    page_in_last_volume = 0
    for page in list_pages_count:
        if page_in_last_volume + page <= mid:
            page_in_last_volume += page
        else:
            volumes_count += 1
            page_in_last_volume = page
            if page > mid:
                volumes_count = n + 1
                break
    volumes_count += 1
    if volumes_count <= n:
        right = mid
    else:
        left = mid


# Запись в выходной файл
output_file.write(str(right))
