# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:03:26 2020

@author: yocoy
"""

def encuentraRepetidos(lista, valor):
    
    indices = []
    
    for i in range(len(lista)):
        if lista[i] == valor:
            indices.append(i)
    return indices


lista = [0,0,5,6,7,8,9,0,7,0]
indices = encuentraRepetidos(lista, 0)
print(indices)
print("Número de veces repetido:", len(indices))

