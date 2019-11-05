#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:41:39 2018

@author: rodrigo
"""

#Porcentaje de residuo parte 2

def get_aa_percentage(protein, aa_list=['A','I','L','M','F','W','Y','V']):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
    percentage = total * 100 / protein_length
    return percentage

assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])==5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L'])==55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP",['F', 'S', 'L'])==70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP")==65

#agregue el mismo ej
p=get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L'])
print(p)