#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:05:27 2018

@author: rodrigo
"""
#Calculo de la secuencia complementaria
#secuencia complementaria
#secuencia ingresada

ADN="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#primero reemplazar

seccomplA=ADN.replace("A","t")

#controles
print(seccomplA)

seccomplC=seccomplA.replace("C","g")

#controles
print(seccomplC)

seccomplG=seccomplC.replace("G","c")

#controles
print(seccomplG)

seccomplT=seccomplG.replace("T","a")

#transformo em mayusculas
ADNcompl=seccomplT.upper()

print("la secuencia complementaria es",ADNcompl)