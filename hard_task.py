#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Даны три слова. Напечатать неповторяющиеся в них буквы.

if __name__=="__main__":
    word_1 = input()
    word_2 = input()
    word_3 = input()

    words_list = []
    for i in word_1:
        if i not in word_2 and i not in word_3:
            words_list.append(i)
    for i in word_2:
        if i not in word_1 and i not in word_3:
            words_list.append(i)
    for i in word_3:
        if i not in word_2 and i not in word_1:
            words_list.append(i)

    print(set(words_list))
            


