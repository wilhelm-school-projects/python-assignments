#!/usr/bin/python3
# -*- coding: utf-8; mode: python; -*-

# 1. Säger vilken version av python vi ska köra och vart den finns i datorn
# 2. Säger åt vilken teckenkodning som ska användas när vi kör programmet.

# Kodstruktur
#   import av bibliotek
#   definitioner av underprogram
#   variabler för huvudprogrammet
#   satser

# Division
# /  resultatet blir ett flyttal
# // heltalsdivision, resultatet blir ett heltal

# if-satser
# if something and something_else then.. kommer endast göra "something_else" jämförelsen om "something" är sant.
# if something or something_else then.. kommer endast göra "something_else" jämförelsen om "something" är falsk.

# Underprogram
# "->" specificerar returtypen 
# def foo(i : int) -> float:        # I parameterlistor ska man visst deklarera med int. Varför?
#     return float(i)

# Variabler
# i = int   # Detta överlagrar typkonverteringsfunktionen "int"
# i = 0     # Detta ger i värdet 0 och typen int

# Lite godtyckligt
#   print("Du matade in: {}".format(name))
#   print("Du matade in:", name)                  # Dessa gör samma sak 
#   print("Du matade in: " +  name)

#   dummy = 100000
#   print("tal:{:10d}".format(dummy))

#   float_dummy = 10.42
#   print("tal:{:8.3f}".format(float_dummy))        # <:> högerjusterat, <8> antal mellanslag, <.3> antal decimaler, <f> typen flyttal

#   string_var.split() returnerar en array av orden i string_var där orden
#   separeras med whitespace




def main() -> None:
    #print("Mata in ett fint namn: ", end = "")      # end = "" säger åt print att inte göra newline
    #name = input()                                  # Läser in från tangentbordsbufferten
    
    word = ""
    number = 0.0

    # word = input("Mata in ett fint namn: ")       # Gör samma sak som de två raderna ovan
    # print("Du matade in ordet: {}".format(word))
    
    # word = input("Mata in ett ord: ")
    # print("Du matade in ordet: {}".format(word))

    # number = int( input("Mata in ett heltal: ") )
    # number += 1
    # print("Talet du matade in plus ett", number)
    # print("Talet du matade in plus ett " + str(number))
    # print("Talet du matade in plus ett {}".format(number))

    word = input("Mata in två ord: ")
    print("Du matade in orden |{}| och |{}|".format( word.split()[0], word.split()[ len(word.split()) - 1 ] ))  # Otydligare kunde jag inte gjort det :D

main()