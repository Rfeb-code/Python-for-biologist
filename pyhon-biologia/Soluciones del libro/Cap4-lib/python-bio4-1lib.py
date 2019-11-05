#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:55:45 2018

@author: rodrigo
"""

# open the input file #LE DI LA DIRECCION DEL ARCHIVO
file = open("/home/rodrigo/Descargas/Python-libros/lists_loops/input.txt")
# open the output file
output = open("trimmed.txt", "w")
# go through the input file one line at a time
for dna in file:
    # calculate the position of the last character
    last_character_position = len(dna)
    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:last_character_position]
    # print out the trimmed sequence
    output.write(trimmed_dna)
    # print out the length to the screen
    print("processed sequence with length " + str(len(trimmed_dna)))