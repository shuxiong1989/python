#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: is_even_num.py

from __future__ import print_function


def is_even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False

s = 0

for i in range(10):
    if is_even_num(i):
        print(i)
        s += 1

print("has ", s, " even number")
