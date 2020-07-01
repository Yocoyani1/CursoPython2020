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
        
    #Regresa true si está muerto o false si el personaje todavía tiene vida
    def morir(self):
        if self.vida <= 0:
            print(self.nombre," se murió")
            return True
        else: 
            return False

#Programa principal

#Creamos una lista de los personajes que queremos en nuestro juego
luchadores = [Personaje("Mario",100,100,500),Personaje("Sonic", 150, 80, 500),Personaje("Link", 200,150,400)]

#Listamos los personajes en pantalla    
for i in range(len(luchadores)):
    print(i+1,")",luchadores[i].nombre)

#Pedimos al usuario que seleccione el primer personaje
while True:
    try:
        seleccion1 = int(input("Primer personaje: "))
        if seleccion1 <= 0 or seleccion1 > len(luchadores):
            print("No existe ese luchador, intenta otra vez")
        else:
            break
    except ValueError:
        print("Carácter no reconocido, intenta otra vez")
#Pedimos al usuario que seleccione el tercer personaje            
while True:
    try:
        seleccion2 = int(input("Segundo personaje: "))
        if seleccion2 <= 0 or seleccion2 > len(luchadores):
            print("No existe ese luchador, intenta otra vez")
        else:
            break
    except ValueError:
        print("Carácter no reconocido, intenta otra vez")

#Asignamos la selección del usuario a luchador 1 y 2
luchador1 = luchadores[seleccion1-1]
luchador2 = luchadores[seleccion2-1]


#print(luchador2.vida)
#Jugador 1 ataca
ataque_oponente = luchador1.atacar()
#Jugador 2 se defiende con base en el ataque oponente
luchador2.defender(ataque_oponente)
#Preguntamos si el luchador 2 murió
luchador2.morir()

#print(luchador2.vida)





