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
    
    seleccion = int(input("-> "))
    
    if seleccion == 5:
        break 
    
    num1 = float(input("Primer número: "))
    
    num2 = float(input("Segundo número: "))
    
     #String + float
     #print(i1,i2,i3,...)
   
    if seleccion == 1:
        print("Resultado: "+str(num1+num2))
    elif seleccion == 2:
        print("Resultado:", num1-num2)
    elif seleccion == 3:
         print("Resultado: "+str(num1*num2))
    elif seleccion == 4:
        while num2 == 0:
            print("Error, no se puede dividir entre 0. Vuelve a ingresar el valor")
            num2 = float(input("Segundo número: "))
        print("Resultado:",num1/num2)
            