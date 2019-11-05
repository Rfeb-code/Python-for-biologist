#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:55:10 2018

@author: rodrigo
"""

#crear 3 archivos fasta

#este es para el archivo 1
#crear y escribir el archivo fasta1
fasta1=open("ABC123.fasta","w")
#la secuencia de adn
sec1="ATCGTACGATCGATCGATCGCTAGACGTATCG"
#escribir el contenido, \n es para el salto de linea
fasta1.write(">ABC123" + '\n' + sec1)

#para el fasta 2
fasta2=open("DEF456.fasta","w")
#transformo a mayusculas
sec2="actgatcgacgatcgatcgatcacgact".upper()
#escribir el contenido de la secuencia 2
fasta2.write(">DEF456" + '\n' + sec2)

#para el fasta 3

fasta3=open("HIJ789.fasta","w")
sec3="ACTGAC-ACTGT--ACTGTA----CATGTG"
#secuencia donde reemplazamos - por espacios en blanco
secrem=sec3.replace("-","")
#escribir el contenido
fasta3.write(">HIJ789" + '\n' + secrem)
