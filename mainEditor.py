# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:03:10 2019

@author: yocoy
"""
#Importa al archivo Edición Luchadores
import EdicionLuchadores as el

#Es una función encargada de pedir los valores a pedir al usuario
#borrar = false significa que borrar tendrá por default el valor de false
#pero si se indica lo contrario cambiará su valor
def pedirValores(borrar = False):
    nombre = input("Nombre Personaje: ")
    if not borrar:
        ataque = input("Ataque: ")
        defensa = input("Defensa: ")
        vida = input("Vida: ")
        return nombre, ataque, defensa, vida
    return nombre

#Despliega siempre el menú
while True:
    #Obtiene la información que contiene el archivo
    lista = el.recuperarArchivo()
    #Despliega el menú
    print("\tPersonajes")
    print("Nombre Ataque Defensa Vida")
    #Recoore la lista con la información y despliega cada renglón
    for personaje in lista:
        print(personaje[0]+' '+personaje[1]+' '+personaje[2]+' '+personaje[3])
    print("1)Crear")
    print("2)Editar")
    print("3)Borrar")
    print("4)Salir")
    accion = input("->")
    
    #Manda llamar a la acción correspondiente dependiendo de la selección del usuario
    if accion == "1":
        nombre, ataque, defensa, vida = pedirValores()
        el.crearPersonaje(nombre, ataque, defensa, vida)
    elif accion == "2":
        nombre, ataque, defensa, vida = pedirValores()
        el.editarPersonaje(nombre, ataque, defensa, vida)
    elif accion == "3":
        nombre = pedirValores(borrar = True)
        el.borrarPersonaje(nombre)
    elif accion == "4":
        break