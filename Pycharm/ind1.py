#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    symb = 2
    while symb < len(s):
        print(s[symb])
        symb += 3
