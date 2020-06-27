# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:34:47 2020

@author: yocoy
"""

class Carro():
    
    #Atributos
    llantas = 0
    marca = ""
    volante = ""
    color = ""
    ventanas = 0
    motor = ""
    
    #Métodos 
    def avanzar(self):
        print("El carro está avanzando")
        
    def reversa(self):
        print("El carro está retrocediendo")
    
carro1 = Carro()
carro1.llantas = 4


print(carro1.llantas)
carro1.avanzar()

carro2 = Carro()
carro2.llantas = 5

print(carro2.llantas)
print(carro1.llantas)