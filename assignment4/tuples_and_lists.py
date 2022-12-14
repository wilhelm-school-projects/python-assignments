#!/usr/bin/python3.9
#-*- coding: utf-8; mode: python; -*-

# För att köra senaste variant av python:
#       1. sudo apt update
#       2. sudo apt install python3.10
#       3. ls /usr/bin | grep python    # To check what versions are available

# def modification_test(seq1: list, seq2: list, i: int) -> None:
#     seq1 = [1, 2, 3]                                    # seq1 objektet uppdateras ej
#     seq2.append("From inside modifictaion_test")        # seq2 objektet uppdateras
#     i = 39                                              # i objektet uppdateras ej

# def main():
#     number_list = [1,2]
#     other_list = ["Hello, 15, 6.23"]
#     number = 9
#     modification_test(number_list, other_list, number)
#     print(number_list)
#     print(other_list)
#     print(number)


# main()

def already_exists(item  : tuple,
                   item_list : list) -> bool:

    return item in item_list

def input_grades(grades_list : list) -> None:

    while(True):
        line = input("Mata in en kurs och ett betyg på fromen kurskod:betyg: ")
        if len(line) == 0:
            print("Klar med inmatningar")
            break
        
        line = line.split(':')
        if len(line) != 2:
            print("Felaktig inmatning, försök igen!")
            continue

        course = line[0]
        grade = int( line[1] )
        current_grade = (course, grade)
        if already_exists(current_grade, grades_list):
            print("Betyget finns redan i listan")
            continue

        grades_list.append(current_grade)

def rapport_grades(grades_list : list,
                   date        : str) -> None:

    for i in range(0, len(grades_list)):
        if len(grades_list[i]) == 3:
            print("{} är redan rapporterad på datum {} med betyg {}".format( grades_list[i][0], grades_list[i][2], grades_list[i][1], ))
            continue
        grades_list[i] = (grades_list[i][0], grades_list[i][1], date)
        print("{} rapporterad med betyg {}".format( grades_list[i][0], grades_list[i][1] ))

def main() -> None:

    grades_list = []
    print("=== Välkommen! Mata in ett av menyvalen. ===")
    print()
    while(True):
        while(True):
            print("1: Mata in kurser och betyg")
            print("2: Gör en rapportering")
            print("0: Avsluta")

            choice = int( input("Mata in ett menyval: ") )
            if 0 <= choice and choice <= 2 :
                break

            print("Felaktigt val, försök igen.")
            print()
        
        if choice == 0:
            print("Programmet avslutas")
            break
        elif choice == 1:
            input_grades(grades_list)
            print()
        elif choice == 2:
            date = input("Mata in ett rapporteringsdatum: ")
            rapport_grades(grades_list, date)
            print()

main()




