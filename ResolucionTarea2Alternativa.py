# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:19:17 2020

@author: yocoy
"""

def encuentraRepetidos(lista, valor):
    
    indices = []
    contador = 0
    
    for i in lista:
        if i == valor:
            indices.append(contador)
        contador += 1
    return indices


lista = [0,0,5,6,7,8,9,0,7,0]
indices = encuentraRepetidos(lista, 0)
print(indices)
print("Número de veces repetido:", len(indices))