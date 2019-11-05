#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:36:51 2018

@author: rodrigo
"""

#Porcentaje de aminoacido parte 2

#definir los aminoacidos hidrofobicos en una lista
def prah(secprot,amhf=["A","I","L","M","F","W","Y","V"]):
    #convertir siempre a mayusculas
    secprot=secprot.upper()
    #longitud sec de proteina
    lsecprot=len(secprot)
    #aat aminoacido total hidrofobico (th)lo inicio en 0 (variable global)
    th=0
    #hacer un ciclo for para contar cada aminoacido de la secuencia de proteina
    for aah in amhf:
        #tambien convertir a mayusculas
        aah=aah.upper()
        
        #significa contar cada aminoacido de amhf en secprot
        #cada ciclo for me da un aminoacido
        aac=secprot.count(aah)
        #le sumo al total
        th=th+aac
        
    #porcentaje de aminocacido total hidrofobico praht
    praht=(th/lsecprot)*100
    praht1=int(praht)
    return praht1
#Nota importante
# si dejo (th/lsecprot)*100 me da un float
#assery ==55 me va a dar error
#por eso convertir a int    
        
assert prah("MSRSLLLRFLLFLLLLPPLP", ["M"])==5
assert prah("MSRSLLLRFLLFLLLLPPLP", ['M', 'L'])==55
assert prah("MSRSLLLRFLLFLLLLPPLP",['F', 'S', 'L'])==70
assert prah("MSRSLLLRFLLFLLLLPPLP")==65

#el porcentraje impreso sera p
#ej
p=prah("MSRSLLLRFLLFLLLLPPLP",["M","L"])
print(p)
