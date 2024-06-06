#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibo_sequence = [0, 1]
        
        while len(fibo_sequence) < length:
            next_number = fibo_sequence[-1] + fibo_sequence[-2]
            fibo_sequence.append(next_number)
            
        print(fibo_sequence)