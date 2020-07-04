# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:49:10 2020

@author: yocoy
"""

#Definición de la clase Personaje
class Personaje():
    
    #Definición del constructor de la clase y sus atributos
    def __init__(self, nombre, ataque, defensa, vida):
        #Asignar Atributos
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        
    #Definición de métodos

    #Imprime que está atacando y regresa el ataque    
    def atacar(self):
        print(self.nombre," está atacando")
        return self.ataque
    
    #Imprime que está defendiendose, calcula el daño y modifica la vida
    def defender(self, ataque_oponente):
        print(self.nombre, " está defendiendose")
        daño = (ataque_oponente/self.defensa)*100
        self.vida -= daño
        
    #Regresa true si está muerto o false si el personaje todavía tiene vida
    def morir(self):
        if self.vida <= 0:
            print(self.nombre," se murió")
            return True
        else: 
            return False


