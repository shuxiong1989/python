#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test_while.py

from __future__ import print_function


while True:
    print("Who are you?")

    name = raw_input()
    if name != 'Joe':
        continue

    print("Hello, Joe, What is the password?(it is a fish.)")
    password = raw_input()
    if password == 'lmx123':
        break
    else:
        print("Error Password")

print("Access granted.")
