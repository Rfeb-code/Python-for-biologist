#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:08:43 2018

@author: rodrigo
"""

#Splicing parte 2
# % de la region que es codificante

DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGAT \
CGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1=(DNA[0:63])
exon2=(DNA[90:])

#region codificante rcod

rcod=exon1+exon2

#longitud de la cadena total y de la region codificante
# lDNA total y lrcod de la parte codificante
#hay que hacer un cambio de str a int
lDNA=int(len(DNA))
lrcod=int(len(rcod))

# % que es codificante rcod_porc

rcod_porc=(lrcod/lDNA)*100

print("el porcentaje de secuencia codificante es", rcod_porc)