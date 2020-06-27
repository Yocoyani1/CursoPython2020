# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:23:46 2020

@author: yocoy
"""

class Carro():
    
    #Constructor
    def __init__(self,llantas,marca,volante,color,ventanas,motor):
        
        #Atributos
        self.llantas = llantas
        self.marca = marca
        self.volante = volante
        self.color = color
        self.ventanas = ventanas
        self.motor = motor
    
    #Métodos
    def avanzar(self):
        print("El carro está avanzando")
        
    def reversa(self):
        print("El carro está retrocediendo")
        
    def subirVentanas(self):
        print("El carro esta subiendo ",self.ventanas," ventanas")
    
    def actualizarColor(self,nuevoColor):
        self.color = nuevoColor
        print("Color cambiado")   
        
    def tocarMusica(self):
        print("Suena la música")
        
        
        
#Creación de objetos        
carro1 = Carro(4,"Mercedez", True,"Azul", 4, "Combustión")
carro1.subirVentanas()
carro1.tocarMusica()

lista_de_carros = [Carro(3,"Toyota",True,"Verde",2,"Eléctrico"),Carro(4,"Tesla",True,"Rojo",4,"Eléctrico")]
print(lista_de_carros[0].marca)
print(lista_de_carros[1].marca)
print(lista_de_carros)


