# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:19:29 2020

@author: yocoy
"""
import math as ma

#tipo nombre = valor;

#Esta línea es un comentario

# print("Hola mundo")
# distancia_entero = 8
# print(type(distancia_entero))

# distancia_cadena = "Hola"
# print(type(distancia_cadena))

# """
# Tipos de variables:
    
#     Enteros -> Int
#     Flotantes(Decimales) -> Float
#     Doubles (Decimales) -> Double
#     Cadena de carácteres(letras y palabras) -> String
#     Booleano -> True o False
# """

# num1 = 3
# num2 = 2
# num3 = 0.58

# print(num1+num2)
# print(num1-num2)
# print(num1/num2)
# print(num1*num2)
# print(num1%num2) #Módulo
# print(num1**num2)
# print(ma.sqrt(num2))#Raíz cuadrada
# print(ma.ceil(num3))#Redondea siempre hacía arriba
# print(ma.trunc(num3))#"Corta" la parte decimal

"""
Abreviación ++ no existe
Abreviación += siginifica que conserva el valor anterior y le suma suma el nuevo valor
Ej: num = 7
num += 5
num ->12
"""


#Condicionales
"""
Operadores Condicionales

== -> Comparación
!= -> Diferente
< -> Menor qué
> -> Mayor qué
<= -> Menor igual
>= -> Mayor igual

and -> Los deben de cumplir
or -> Con uno que cumpla
not -> Lo contrario 

***** El resultado es un booleano

"""
# num1 = 2
# num2 = 1

# resultado = num2>num1

# print(resultado)

control = False
num = 4

# print(type(control))

# if num == 5:
#     print("Número = 5")
#     print("Se cumplio la condición")
# elif num != 4:
#     print("Número es igual a 4")
# else:
#     print("Número no es igual a 5 y es 4")
    
# if not control: 
#     print("1")
# elif control == True:
#     print("2")
# else:
#     print("3")

#Ciclos 
#Una serie de instrucciones que se repiten un determinado número de veces

#While ->No conozco cuantas veces se va a repetir
#For ->Conocemos cuantas veces se va a repetir

# lectura = 9

 # while True:
 #     lectura += 1
 #     if lectura == 20:
 #         break
 #     continue
 #     print(lectura)
    
# print(lectura)
# print("Hola")

"""
for indice in objeto_contable:
    Código
    
89,1,2,3,4,5
89
1
2
3
4
5
Termina for
"hola"

range(valor)-> Genera un objeto contable, de tamaño igual a valor
              por default lo genera desde 0 hasta valor-1  

"""

# for x in range(9):
#     print(x)

# lista = ["pera","manzana","uva","naranja"]

# # for x in "Hola":
# #     print(x)

# for x in lista:
#     print(x)
#     if x == "uva":
#         break

#Entrada de datos
decision = input("Introduce tu decisión: ")

print(decision)
print(type(decision))

decision_en_numero = int(decision) #Casteo->Convertir tipos de variable
print(decision_en_numero)
print(type(decision_en_numero))


"""
Como void loop() -> while True:
    str(valor)->casteo a string
"""

print("Hola "+"Mundo")























































