#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


if __name__ == "__main__":
    try:
        matrix = []
        a, b = int(input('Введите число строк: ')), int(input('Столбцы: '))
        range_start, range_end = int(input('Диапазон: ')), int(input('Диапазон: '))

        for i in range(a):
            row = []
            for _ in range(b):
                row.append(random.randint(range_start, range_end))
            matrix.append(row)
        print(matrix)
    except ValueError:
        print('Ошибка ввода! Вводите только целые числа!')