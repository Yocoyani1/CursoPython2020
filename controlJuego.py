# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:12:56 2020

@author: yocoy
"""

from Personaje import Personaje
from random import randint

def controlJuego(luchador1,luchador2):
    turno = 0
    while not luchador1.morir() and not luchador2.morir():
        
        print("Vida ",luchador1.nombre,":",luchador1.vida)
        print("Vida ",luchador2.nombre,":",luchador2.vida)
        
        if turno % 2 == 0:
            print("Turno jugador 1")
            input("Presione enter para atacar")
            if randint(0,100) > 35:
                ataque_oponente = luchador1.atacar()
                luchador2.defender(ataque_oponente)
            else:
                print(luchador2.nombre," esquivó el ataque")
                
        else:
            print("Turno jugador 2")
            input("Presione enter para atacar")
            if randint(0,100) > 35:
                ataque_oponente = luchador2.atacar()
                luchador1.defender(ataque_oponente)
            else:
                print(luchador1.nombre," esquivó el ataque")
        turno += 1  