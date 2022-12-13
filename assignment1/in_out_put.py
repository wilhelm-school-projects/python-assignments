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

#   "{1} {0}".format(arg0, arg1) för att indexera argumenten
#   float_dummy = 10.42
#   print("tal:{:8.3f}".format(float_dummy))        # <:> högerjusterat, <8> antal mellanslag, <.3> antal decimaler, <f> typen flyttal

#   string_var.split() returnerar en array av orden i string_var där orden
#   separeras med whitespace




def main() -> None:
    #print("Mata in ett fint namn: ", end = "")      # end = "" säger åt print att inte göra newline
    #name = input()                                  # Läser in från tangentbordsbufferten
    
    line = ""

    line = input("Mata in ett fint namn: ")       # Gör samma sak som de två raderna ovan
    print("Du matade in ordet: {}".format(line))
    print()

    line = input("Mata in ett ord: ").split()
    print("Du matade in ordet: {}".format(line[0]))
    print()

    line = input("Mata in ett heltal: ").split()
    print("Talet du matade in plus ett", int(line[0]) + 1)
    print("Talet du matade in plus ett " + str(int(line[0]) + 1) )
    print("Talet du matade in plus ett {}".format( str(int(line[0]) + 1) ))
    print()

    line = input("Mata in två ord: ").split()
    print("Du matade in orden |{}| och |{}|.".format( line[0], line[1] ))
    print()

    line = input("Mata in fem heltal: ")
    print("Talen du matade in minus fem: {} {} {} {} {} ".format( int(line.split()[0]) - 5, int(line.split()[1]) - 5, int(line.split()[2]) - 5,
                                                                    int(line.split()[3]) - 5, int(line.split()[4]) - 5, ))
    print()

    # Det verkar som man måste ha alla om man ska ha någon ":", "0", "." och "f"
    line = input("Mata in ett flyttal: ").split()
    print("DU matade in flyttalet: {:0.3f}".format( float(line[0]) ))    
    print()

    # Det går ju att köra split direkt också
    line = input("Mata in två heltal och ett flyttal: ").split()        
    print("Det första heltalet var: {:8d}".format( int(line[0]) ))
    print("Det andra heltalet var: {:.>8d}".format( int(line[1])))
    print("Det första heltalet var: {:8.4f}".format( float(line[2]) ))
    print()

    line = input("Mata in ett heltal och ett ord: ").split()
    print("Talet du matade in delat på två är |{}| och ordet var |{}|.".format( int(line[0]) // 2, line[1] ))
    print()

    line = input("Mata in ett ord och ett flyttal: ").split()
    print("FLyttalet plus 2 är \"{:0.3f}\" och ordet är \"{}\"".format( float(line[1]) + 2, line[0] ))
    print()

main()