#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0: # To print empty list
        print([])
    elif length == 1: # Checking whether input is 1, if so, print number 0
        print([0])
    else:
        fibo_sequence = [0, 1] # If input is neither 0 nor 1, initialize fibo_sequence list with the first two Fibonacci numbers.
        
        while len(fibo_sequence) < length: # While loop will continue until length of fibo_sequence is equal to the input length.
            next_number = fibo_sequence[-1] + fibo_sequence[-2] # This function calculates the next Fibonacci number by adding the last two numbers in fibo_sequence.
            fibo_sequence.append(next_number) # This is to append the calculated number to the fibo_sequence List.
            
        print(fibo_sequence)