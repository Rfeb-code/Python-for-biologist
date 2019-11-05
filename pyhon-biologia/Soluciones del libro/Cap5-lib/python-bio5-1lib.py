#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:20:44 2018

@author: rodrigo
"""

#Porcentaje de  residuo de aminoacido

def get_aa_percentage(protein, aa):
   # convert both inputs to upper case
   protein = protein.upper()
   aa = aa.upper()
   aa_count = protein.count(aa)
   protein_length = len(protein)
   percentage = aa_count * 100 / protein_length
   return percentage

# test the function with assertions
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP","M")==5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP","r")==10
assert get_aa_percentage("msrslllrfllfllllpplp","L")==50
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP","Y")==0

