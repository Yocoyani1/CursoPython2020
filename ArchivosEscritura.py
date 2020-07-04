# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:59:24 2020

@author: yocoy
"""

archivo = open('archivo_de_prueba.txt','w') #Abrimos el archivo en modalidad escritura

print("Archivo abierto")

archivo.write("Hola\n"+"Mundo")
# archivo.writelines(["Hola","Mundo"])
# archivo.writelines(["Hola","Mundo"])


archivo.close() #Cerrar archivo