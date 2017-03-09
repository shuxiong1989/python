#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: guess_num.py


import random


def again():
    char = raw_input("Do you want to continue?Please input yes or no!!!!!")
    if char == 'yes':
        main()
    elif char == 'no':
        print("Good bye!!!!")
        exit()
    else:
        print("Oh, No......")
        exit()


def play_game(num):
    while True:
        a = int(raw_input("Please input a number: "))
        if a > num:
            print("The number is bigger")
        elif a < num:
            print("The number is smaller")
        else:
            print("You are right!")
            again()


def main():
    print("------------------begin game----------------------")
    num = random.randint(0, 99)
    #print(num)  # 调试
    play_game(num)


if __name__ == '__main__':
    main()


