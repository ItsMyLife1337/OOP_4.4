#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a, b = input(), input()

    try:
        print('Сумма чисел:', float(a + b))
    except:
        print('Конкатенация', a + b)
