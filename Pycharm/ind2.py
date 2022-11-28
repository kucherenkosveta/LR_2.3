#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    if 'чу' in s:
        ind_chu = s.find('чу')
    if 'щу' in s:
        ind_shu = s.find('щу')
    print(min(ind_shu, ind_chu))
