#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести все имеющиеся в нем буквосочетания нн.

if __name__=="__main__":
    substring = 'Ваше предложение с буквосочетанием нн и еще немного нн.'

    for i in range(len(substring) - 1):
        if substring[i:i+2] == "нн":
            print(f"{i}:{i+2} == нн" , end="\n")
