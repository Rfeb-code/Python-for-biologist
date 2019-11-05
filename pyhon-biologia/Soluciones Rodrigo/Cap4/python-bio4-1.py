#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:53:54 2018

@author: rodrigo
"""

#Procesando adn en un archivo
#abro elarchivo y coloco la direccion

arch_adn=open("/home/rodrigo/Descargas/Python-libros/lists_loops/input.txt")

#NOTA IMPORTANTE!: si lo abria para lectura no andaba

#abro y creo un  nuevo archivo
arch_clean=open("arch_clean1","w")

#para cada secuencia en el archivo arch_adn
for seq in arch_adn:
    #archivo limpio (las 14 1ra son adapter)
    #desde la posicion 14 hasta el final
    seqc=seq[14:]
    #lo escribo en arc_clean1
    arch_clean.write(seqc)
    