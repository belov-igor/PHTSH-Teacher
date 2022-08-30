# -*- coding: utf-8 -*-

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


text = 'avada kedavra'
print(prefix_function(text))
