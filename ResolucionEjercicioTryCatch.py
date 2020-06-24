# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:07:48 2020

@author: yocoy
"""


while True:
     
    #\t -> De un espacio de tabulador
    print("\tMenú")
    print("1)Suma")
    print("2)Resta")
    print("3)Multiplicación")
    print("4)División")
    print("5)Salir")
    
    while True:
        try:
            seleccion = int(input("-> "))
            break
        except ValueError:
            print("Error, intentalo de nuevo")
    
    if seleccion == 5:
        break 
    
    while True:
        try:
            num1 = float(input("Primer número: "))
            break
        except ValueError:
            print("Introduce un número válido!!")
    
    while True:
        try:
            num2 = float(input("Segundo número: "))
            break
        except ValueError:
            print("Introduce un número válido!!")
     
  
    if seleccion == 1:
        print("Resultado: "+str(num1+num2))
    elif seleccion == 2:
        print("Resultado:", num1-num2)
    elif seleccion == 3:
         print("Resultado: "+str(num1*num2))
    elif seleccion == 4:
        while True:
            try:
                num1/num2
                break
            except ZeroDivisionError:
                
                print("Error, no se puede dividir entre 0. Vuelve a ingresar el valor")
                while True:
                    try:
                        num2 = float(input("Segundo número: "))
                        break
                    except ValueError:
                        print("Introduce un número válido!!")
        
        print("Resultado:",num1/num2)
            