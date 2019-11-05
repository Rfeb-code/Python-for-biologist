#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 07:32:59 2018

@author: rodrigo
"""

#Porcentaje de residuos de aminoacidos

#Funcion pra(porcentaje de residuo de aminoacido)

def pra(secprot,aminoacido):
    #convertir siempre a mayusculas
    secprot=secprot.upper()
    aminoacido=aminoacido.upper()
    #longitud sec de proteina
    lsecprot=len(secprot)
    #cantidad de residuos del aminoacido como variable sin comillas
    c_aminoacido=secprot.count(aminoacido)
    #porcentaje
    prami=(c_aminoacido/lsecprot)*100
    return prami

assert pra("MSRSLLLRFLLFLLLLPPLP", "M")==5
assert pra("MSRSLLLRFLLFLLLLPPLP", "r")==10
assert pra("msrslllrfllfllllpplp","L")==50
assert pra("MSRSLLLRFLLFLLLLPPLP","Y")==0

#el porcentraje impreso sera pra_i

pra_i=pra("MSRSLLLRFLLFLLLLPPLP", "M")

print(pra_i)