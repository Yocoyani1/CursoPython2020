# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:24:56 2020

@author: yocoy
"""

archivo = open("archivo_de_prueba.txt","r") #Abrimos el archivo como lectura

lectura = archivo.readlines()

archivo.close()

print(lectura)

lectura[0] = lectura[0].split('l')
print(lectura)

lectura[0][0] = lectura[0][0].replace('o','a')

print(lectura)