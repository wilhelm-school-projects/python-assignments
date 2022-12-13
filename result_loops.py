#!/usr/bin/python3
# -*- coding: utf-8; mode: python; -*-

import random
def game(lower_limit : int, 
         upper_limit : int,
         step        : int, 
         guesses     : int) -> None:
    print("########## GISSNINGSSPELET ##########")
    
    random_val = random.randrange(lower_limit, upper_limit, step)
    current_guess = 0
    for i in range(0, guesses):
        current_guess = int( input("Mata in din gissning: ") )
        
        if current_guess < random_val:

            if current_guess > lower_limit:
                lower_limit = current_guess
            
            print("Du gissade för lågt! ", end = "")
            print("Gissa mellan {} och {}".format( lower_limit, upper_limit ))

        if current_guess > random_val:

            if current_guess < upper_limit:
                upper_limit = current_guess
            
            print("Du gissade för högt! ", end = "")
            print("Gissa mellan {} och {}".format( lower_limit, upper_limit ))

        if current_guess == random_val:
            print("Du vann! Grattis!")
            break
    


def main() -> None:
    random.seed(123456)     # Bara relevant i detta fall med tanke på automaträttningen
    lower_limit = 0
    upper_limit = 0
    step        = 0
    guesses     = 0

    while(True):
        while(True):          
            while(True):
                try:
                    lower_limit = int( input("Nedre gräns: ") )
                    break
                except ValueError:
                    print("Fel datatyp!")

            if lower_limit >= 0:
                break
            print("Felaktigt värde")
        
        while(True):
            while(True):
                try:
                    upper_limit = int( input("Övre gräns: ") )
                    break
                except ValueError:
                    print("Fel datatyp!")
            
            if upper_limit >= lower_limit:
                break
            print("Felaktigt värde")

        while(True):
            try:
                step = int( input("Steglängd: ") )
                break
            except ValueError:
                print("Fel datatyp!")

        if step <= 0 or step > (upper_limit - lower_limit):
            print("För stor steglängd för detta intervall. Försök igen.")
        else:
            while(True):
                while(True):
                    try:
                        guesses = int( input("Mata in antal gissningar: ") )
                        break
                    except ValueError:
                        print("Fel datatyp!")
                
                if guesses > 0:
                    break
                print("Felaktigt värde")
            
            break   

    game(lower_limit, upper_limit, step, guesses)



main()
