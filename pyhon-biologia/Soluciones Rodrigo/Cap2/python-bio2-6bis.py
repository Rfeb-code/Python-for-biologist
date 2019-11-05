#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:23:14 2018

@author: rodrigo
"""

#Splicing parte 3: sec exonicas e intronicas de una cadena

DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1=(DNA[0:64])
intron=(DNA[64:90])
exon2=(DNA[90:])

#pconvertir todo a minuscula
intron_low=intron.lower()

#secuencia completa sc
sc=exon1+intron_low+exon2

print("la secuencia quedaria: ", sc)