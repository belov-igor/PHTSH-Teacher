# -*- coding: utf-8 -*-

def string_equals(text, substring, i):
    """
    :param text:
    :param substring:
    :param i:
    :return:
    """
    return substring == text[i: i + len(substring)]


def substring_search(text, substring):
    """
    Находит индекс вхождения подстроки в строке
    :param text: требуемая строка (текст)
    :param substring:
    :return:
    """
    result = []
    for i in range(len(text) - len(substring)):
        if string_equals(text, substring, i):
            result.append(i)
    return result

