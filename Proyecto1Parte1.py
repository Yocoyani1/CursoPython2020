# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:31:26 2020

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
        
    def morir(self):
        if self.vida <= 0:
            print(self.nombre," se murió")
            return True
        else: 
            return False

luchadores = [Personaje("Mario",100,100,500),Personaje("Sonic", 150, 80, 500),Personaje("Link", 200,150,400)]
    
for i in range(len(luchadores)):
    print(i+1,")",luchadores[i].nombre)
    
while True:
    try:
        seleccion1 = int(input("Primer personaje: "))
        if seleccion1 <= 0 or seleccion1 > len(luchadores):
            print("No existe ese luchador, intenta otra vez")
        else:
            break
    except ValueError:
        print("Carácter no reconocido, intenta otra vez")
            
while True:
    try:
        seleccion2 = int(input("Segundo personaje: "))
        if seleccion2 <= 0 or seleccion2 > len(luchadores):
            print("No existe ese luchador, intenta otra vez")
        else:
            break
    except ValueError:
        print("Carácter no reconocido, intenta otra vez")

luchador1 = luchadores[seleccion1-1]
luchador2 = luchadores[seleccion2-1]

print(luchador2.vida)

ataque_oponente = luchador1.atacar()
luchador2.defender(ataque_oponente)
luchador2.morir()

print(luchador2.vida)





