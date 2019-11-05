#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 07:10:35 2018

@author: rodrigo
"""

#Longitud de los fragmentos de restriccion

DNA="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#La secuencia contiene un sitio de reconocimiento para la enzima de restricción
# EcoRI, que corta en el motivo G * AATTC

#longitud de la cadena total de ADN

lDNA=len(DNA)

#posicion del sitio de corte psc
psc=DNA.find("GAATTC")

#pero como corta una posicion despues tenemos que sumar 1

psc1=psc+1

#debemos extraer los segmentos de la cadena
#seg1 segmento1
#seg2 segmento 2

seg1=DNA[0:psc1]
seg2=DNA[psc1:]

#las secuencias que quedan despues del corte
print("el segmento 1 es",seg1)
print("el segmento 2 es",seg2)


#longitud de los segmentos

lse1=len(seg1)
lse2=len(seg2)

print("la longitud del segmento 1 es",lse1)
print("la longitud del segmento 2 es",lse2)
print("la longitud total de la cadena de ADN es",lDNA)