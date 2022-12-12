#!/usr/bin/python3
# -*- coding: utf-8; mode: python; -*-

def main() -> None:
    word = ""
    number = 0.0

    word = input("Mata in två ord: ")
    if len(word) != 2:
        print("Wrong number of words!")
        return
    print("Du matade in orden |{}| och |{}|".format( word.split()[0], word.split()[ len(word.split()) - 1 ] ))  # Otydligare kunde jag inte gjort det :D

main()
