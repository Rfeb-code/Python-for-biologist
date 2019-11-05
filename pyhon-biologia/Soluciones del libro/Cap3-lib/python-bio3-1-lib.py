#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:59:52 2018

@author: rodrigo
"""
#NOTA ES LA SOLUCION DEL LIBRO: VA A DAR ERROR PORQUE NO EXISTE LA RUTA
#DEL ARCHIVO genomic_dna.txt

# open the file and read its contents
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()
# extract the different bits of DNA sequence
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
# open the two output files
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")
# write the sequences to the output files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)