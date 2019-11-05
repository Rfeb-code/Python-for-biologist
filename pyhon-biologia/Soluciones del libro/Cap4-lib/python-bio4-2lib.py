#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:46:37 2018

@author: rodrigo
"""

#Multiples exones d eun fragmento de ADN

# open the genomic dna file and read the contents #LE DI LA DIRECCION DEL ARCHIVO
genomic_dna = open("/home/rodrigo/Descargas/Python-libros/lists_loops/genomic_dna.txt").read()
# open the exons locations file
exon_locations = open("/home/rodrigo/Descargas/Python-libros/lists_loops/exons.txt")
# create a variable to hold the coding sequence
coding_sequence = ""
# go through each line in the exon locations file
for line in exon_locations:
    # split the line using a comma
    positions = line.split(',')
    # get the start and stop positions
    start = int(positions[0])
    stop = int(positions[1])
    # extract the exon from the genomic dna
    exon = genomic_dna[start:stop]
    # append the exon to the end of the current coding sequence
    coding_sequence = coding_sequence + exon
# write the coding sequence to an output file
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()