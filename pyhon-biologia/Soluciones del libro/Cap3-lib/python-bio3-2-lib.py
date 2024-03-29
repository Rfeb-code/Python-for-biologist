#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:02:58 2018

@author: rodrigo
"""

#ESCRIBIENDO ARCHIVOS FASTA

# set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables
seq_1= "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2= "actgatcgacgatcgatcgatcacgact"
seq_3= "ACTGAC-ACTGT—ACTGTA----CATGTG"

# make a new file to hold the output
output = open("sequences.fasta", "w")
# write the header and sequence for seq1
output.write('>' + header_1 + '\n' + seq_1 + '\n')
# write the header and uppercase sequences for seq2
output.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
# write the header and sequence for seq3 with hyphens removed
output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')



