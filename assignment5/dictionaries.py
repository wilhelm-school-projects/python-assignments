#!/usr/bin/python3.9

# Dictionaries can not be assumed to be sorted by the key as default.

def input_results(results : dict) -> None:

    name = input("Mata in namn: ")
    while(True):
        num_of_hits = int( input("Mata in antal slag: ") )
        if 0 < num_of_hits:
            break
        print("Antal slag måste vara ett positivt heltal. Försök igen.")
    
    if name not in results:
        results.update({name : num_of_hits})
    else:
        results[name] += num_of_hits

def sorted_keys(results : dict) -> list:
    return sorted( results.keys() )

def print_dictionaries(results : dict) -> None:

    print("========= Alla deltagare ===========")
    sorted_keys = sorted( results.keys() ) 
    for key in sorted_keys:
        print("Namn: {:.<10} - Poäng: {:.>10d}".format( key, results[key] ) )


def find_leader(results : dict) -> tuple:
    
    sorted_by_hits = {}
    sorted_values = sorted( results.values() )
    for key in sorted_keys(results):
        if results[key] == sorted_values[0]:
            return (key , results[key])
    
    # returning None to indicate no leader was found


def print_leader(leader : tuple) -> None:
    if leader is None:
        print("Det finns inga spelare!")
        return
    key, value = leader
    print("{} leder just nu med {} poäng".format( key, value ))

def main() -> None:
    print("Minigolf!")
    results = {}
    while(True):
        print("1: Mata in ett nytt resultat\n2: Skriv ut tabellen med totala poäng\n3: Skriv ut nuvarande ledare\n0: Avsluta")
        
        try:
            choice = int( input("Mata in ett menyval: ") )
        except:
            print("Felaktigt val, försök igen.")
            print()
            continue

        if choice < 0 or 3 < choice:
            print("Felaktigt val, försök igen.")
            print()
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
