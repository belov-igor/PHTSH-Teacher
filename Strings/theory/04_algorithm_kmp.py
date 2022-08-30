# -*- coding: utf-8 -*-

def prefix_function(string):
    n = len(string)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and string[j] != string[i]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(string, substring, start_index=0):
    j = 0
    pi = prefix_function(substring)
    for i in range(start_index, len(string)):
        while j > 0 and string[i] != substring[j]:
            j = pi[j - 1]
        if string[i] == substring[j]:
            j += 1
        if j >= len(substring):
            return i - j + 1
    return None


result = []
text = 'ababbababa'  # из задачи 02_substring.py
sub = 'aba'
start = 0


while start <= len(text) - len(sub):
    search = kmp_search(string=text, substring=sub, start_index=start)
    result.append(search)
    start = search + 1

print(result)

