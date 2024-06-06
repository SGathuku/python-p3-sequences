#!/usr/bin/env python3

def print_fibonacci(length):
    fibo_sequence = [0, 1]

    while len(fibo_sequence) < length:
        next_number = fibo_sequence[-1] + fibo_sequence[-2]
        fibo_sequence.append(next_number)

    for num in fibo_sequence:
        print(num)

print_fibonacci(15)
