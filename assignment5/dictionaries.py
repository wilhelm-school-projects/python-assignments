#!/usr/bin/python3.9





def input_results(results : dict) -> None:

    name = input("Mata in namn: ")
    while(True):
        num_of_hits = int( input("Mata in antal slag: ") )
        if 0 < num_of_hits:
            break
        print("Antal slag måste vara ett positivt heltal. Försök igen.")
    
    results.update({name : num_of_hits})


def print_dictionaries(results : dict) -> None:

    print("========= Alla deltagare ===========")
    for key in results:
        print("Namn: {:.<10} - Poäng: {:.>10d}".format( key, results[key] ) )


def find_leader(results : dict) -> dict:
    
    sorted_by_hits = {}
    print( results.values() )

    return {'none' : 0}

def print_leader(leader : dict) -> None:
    print(leader)

def main() -> None:
    print("Minigolf!")
    results = {}
    while(True):
        print("1: Mata in ett nytt resultat\n2: Skriv ut tabellen med totala poäng\n3: Skriv ut nuvarande ledare\n 0: Avsluta")
        choice = int( input("Mata in ett menyval: ") )
        if choice < 0 or 3 < choice:
            print("Mata in igen")
            continue

        if choice == 1:
            input_results(results)
            print()
        elif choice == 2:
            print_dictionaries(results)
            print()
        elif choice == 3:
            print_leader( find_leader(results) )
            print()
        elif choice == 0:
            print("Programmet avslutas")
            break








main()
