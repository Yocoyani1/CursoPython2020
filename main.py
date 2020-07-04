# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:49:34 2020

@author: yocoy
"""
from Personaje import Personaje
from controlJuego import controlJuego

def main():    
    #Creamos una lista de los personajes que queremos en nuestro juego
    luchadores = [Personaje("Mario",100,100,500),Personaje("Sonic", 150, 80, 500),
                  Personaje("Link", 200,150,400),Personaje("Luigi", 300, 100, 150)]
    
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
    #Pedimos al usuario que seleccione el segundo personaje            
    while True:
        try:
            seleccion2 = int(input("Segundo personaje: "))
            if seleccion2 <= 0 or seleccion2 > len(luchadores):
                print("No existe ese luchador, intenta otra vez")
            else:
                break
        except ValueError:
            print("Carácter no reconocido, intenta otra vez")
    
    #Asignar selección del usuario creando dos objetos independientes
    luchador1 = Personaje(luchadores[seleccion1-1].nombre,luchadores[seleccion1-1].ataque,luchadores[seleccion1-1].defensa,
                           luchadores[seleccion1-1].vida)
    
    luchador2 = Personaje(luchadores[seleccion2-1].nombre,luchadores[seleccion2-1].ataque,luchadores[seleccion2-1].defensa,
                           luchadores[seleccion2-1].vida)
    
    controlJuego(luchador1,luchador2)
    
main()