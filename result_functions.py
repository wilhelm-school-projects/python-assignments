#!/usr/bin/python3
# -*- coding: utf-8; mode: python; -*-

def letter_representation(N : int) -> str:
    return chr( ord('a') + N - 1 )         # Off by one since I want the interval ['a','z'] and not ]'a','z'[    

def faculty(N : int) -> int:
    if N == 0:
        return 1
    else:
        return N * faculty(N - 1)

def fib(N : int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N - 1) + fib(N - 2)

def print_table(N : int) -> None:
    print(" N     Bokstav N     N-fakultet     Fibonacci")
    for i in range(1, N + 1):
        print("{:>2}{:>10} {:>14d}{:>14d}".format( i, letter_representation(i), faculty(i), fib(i) ))

while(True):
    N = int( input("Mata in ett tal i intervallet 1-26:") )
    if 1 <= N and N <= 26:
        break
    print("Felaktigt värde, försök igen!")

print_table(N)
