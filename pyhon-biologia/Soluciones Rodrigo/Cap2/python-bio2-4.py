#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:07:10 2018

@author: rodrigo
"""

#Splicing de los intrones parte 1
#secuencia de ADN total

DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGAT \
CGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#ojo python cuenta desde la posicion 0 
exon1=(DNA[0:63])
exon2=(DNA[90:])

#region codificante rcod

rcod=exon1+exon2

print("la region codificante es: ",rcod)

