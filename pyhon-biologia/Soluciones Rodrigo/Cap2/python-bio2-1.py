#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:18:14 2018

@author: rodrigo
"""

#calcular el contenido de AT

#cadena de adn
DNAseq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#encontrar la cantidad de A y T
DNA_A=DNAseq.count("A")
DNA_T=DNAseq.count("T")

#calcular la longitud de la cadena total
DNA_len=len(DNAseq)
#suma de A y T
DNA_AT=DNA_A+DNA_T
#calcular el procentaje
porcAT=(DNA_AT/DNA_len)*100

print("el porcentajes es",porcAT)

