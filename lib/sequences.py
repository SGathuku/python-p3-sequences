#!/usr/bin/env python3

def print_fibonacci(length):
    x, y = 0, 1
    for _ in range(length): #Used the variable (_) after "for" as a placeholder for the loop variable, indicatting that it isn't going to be used.
        print(x)
        x, y = y, x + y

print_fibonacci(15)
