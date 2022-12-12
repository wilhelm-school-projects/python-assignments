#!/usr/bin/python3
# -*- coding: utf-8; mode: python; -*-

# Sorry for all the newlines above. My script 
# for removing only-comment-rows isn't very sophisticated.














def main() -> None:
    
    word = ""
    number = 0.0

    


    word = input("Mata in två ord: ")
    print("Du matade in orden |{}| och |{}|".format( word.split()[0], word.split()[ len(word.split()) - 1 ] ))  # Otydligare kunde jag inte gjort det :D

main()
