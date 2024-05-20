#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 11
    while countdown > 0:
        print(f"{countdown}")
        countdown -= 1
        if countdown == 0:
            print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
