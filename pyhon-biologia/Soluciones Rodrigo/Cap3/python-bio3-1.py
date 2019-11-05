#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:53:48 2018

@author: rodrigo
"""

#Splicing de genomas: escribir en archivos separados
#NOTA IMPORTANTE: ruta con espacio daria error, no encontraria el directorio

#abrir el archivo
mi_archivo=open("/home/rodrigo/Descargas/genomic_dna.txt")
#leer el contenido del archivo
archivo_contenido=mi_archivo.read()

exon1=archivo_contenido[0:64]
intron=archivo_contenido[64:90]
exon2=archivo_contenido[90:]

#secuencia codificante
scod=exon1+exon2

#crear los 2 archivos de salida, abrir y escribir (w)
archivo_cod = open("dna_cod.txt", "w")
archivo_nocod = open("dna_nocod.txt", "w")

# escribir la secuencias dentro de los archivos
archivo_cod.write(scod)
archivo_nocod.write(intron)