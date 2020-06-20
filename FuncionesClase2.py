# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:18:41 2020

@author: yocoy
"""
"""
def nombre(párametros(opcionales)):
    Código
    return valor (Opcional)-> Regresa el valor solicitado y termina la ejecución de la función 

""" 

def saludo(nombre):
    print("Hola, ten un buen día",nombre)
    
def redondeo(valor):
    valor_entero = int(valor)
    criterio_redondeo = valor-valor_entero
    
    if criterio_redondeo == 0:
        return valor
    if criterio_redondeo <= 0.5:
        return valor_entero
    else:
        return valor_entero+1


# saludo("Yocoyani")
numero_redondeado = redondeo(8.9)
numero = redondeo(7.8)
numero2 = redondeo(7.4)

print(numero_redondeado)
print(numero)
print(numero2)