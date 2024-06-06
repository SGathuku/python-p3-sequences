#!/usr/bin/env python3

def print_fibonacci(length):
    fibo_sequence = [0, 1]

    while len(fibo_sequence) < length:
        next_number = fibo_sequence[-1] + fibo_sequence[-2]
        fibo_sequence.append(next_number)

    for number in fibo_sequence:
        print(number)

print_fibonacci(15)
