#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:25:22 2018

@author: rodrigo
"""
#EXONES MULTIPLES DE UN FRAGMENTO DE ADN

#es un archivo que tiene la sec de adn y lo leo con el metodo read
arch_adn=open("/home/rodrigo/Descargas/Python-libros/lists_loops/genomic_dna.txt").read()
#es un archivo que tiene la posicion de los exones
arch_adn_exon=open("/home/rodrigo/Descargas/Python-libros/lists_loops/exons.txt")

#abro y creo un  nuevo archivo 
arch_exon_pos=open("arch_exon1","w")

#crear una variable con la secuencia codificante

sec_cod=""

#extraigo las posiciones de los exones

for exon_pos in arch_adn_exon:
    #meter en una lista de 2 elementos(inicio;fin)
    #remuevo split
    exon_postodo=exon_pos.split(',')
    
    #extraer las posiciones
    #convertir de str a int
    inicio=int(exon_postodo[0])
    fin=int(exon_postodo[1])
    
    #extraigo los exones del archivo
    exons=arch_adn[inicio:fin]
    
    #agrego los exones a la secuencia codificante sec_cod
    
    sec_cod=sec_cod + exons
    
#excribo la secuencia en el archivo  arch_exon1
    
arch_exon_pos.write(sec_cod)

#cierro el archivo
arch_exon_pos.close
    
   
