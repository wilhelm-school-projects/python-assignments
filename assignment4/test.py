#!/usr/bin/python3.9

def modification_test(seq1: list, seq2: list, i: int) -> None:
    seq1 = [1, 2, 3]
    seq2.append("From inside modifictaion_test")
    i = 39

def main():
    number_list = [1,2]
    other_list = ["Hello, 15, 6.23"]
    number = 9
    modification_test(number_list, other_list, number)
    print(number_list)
    print(other_list)
    print(number)

main()