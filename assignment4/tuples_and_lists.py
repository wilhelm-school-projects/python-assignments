#!/usr/bin/python3.9
#-*- coding: utf-8; mode: python; -*-

# För att köra senaste variant av python:
#       1. sudo apt update
#       2. sudo apt install python3.10
#       3. ls /usr/bin | grep python    # To check what versions are available



def modification_test(seq1: list, seq2: list, i: int) -> None:
    seq1 = [1, 2, 3]                                    # seq1 objektet uppdateras ej
    seq2.append("From inside modifictaion_test")        # seq2 objektet uppdateras
    i = 39                                              # i objektet uppdateras ej

def main():
    number_list = [1,2]
    other_list = ["Hello, 15, 6.23"]
    number = 9
    modification_test(number_list, other_list, number)
    print(number_list)
    print(other_list)
    print(number)


main()


# def input_grades() -> List[(str, int)]:

# def main() -> None:
#     grades_list = []
#     while(True):
#         print("=== Välkommen! Mata in ett av menyvalen. ===")
#         while(True):
#             print("1: Mata in kurser och betyg")
#             print("2: Gör en rapportering")
#             print("0: Avsluta")

#             choice = int( input("Mata in ett menyval: ") )
#             if 0 <= choice and choice <= 3 :
#                 break

#             print("Felaktigt val, försök igen.")
#             print()
        
#         if choice == 0:
#             print("Programmet avslutas")
#             break
#         elif choice == 1:
#             print()
#         elif choice == 2:
#             print()






