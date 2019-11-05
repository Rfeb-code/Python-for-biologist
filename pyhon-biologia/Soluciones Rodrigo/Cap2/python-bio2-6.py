#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:13:50 2018

@author: rodrigo
"""

#Splicing parte 3: sec exonicas e intronicas de una cadena

DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1=(DNA[0:64])
intron=(DNA[64:90])
exon2=(DNA[90:])


#primero reemplazar

intronA=DNA.replace("A","a")

#controles
print(intronA)

intronC=intronA.replace("C","c")

#controles
print(intronC)

intronG=intronC.replace("G","g")

#controles
print(intronG)

intronT=intronG.replace("T","t")

#intron total intront
intront=intronT

#secuencia completa sc

sc=exon1+intront+exon2

print("la secuencia quedaria: ", sc)