# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:10:26 2019

@author: yocoy
"""

#Archivo que guarda los luchadores con el formato

"""
Nombre Ataque Defensa Vida
Nombre Ataque Defensa Vida
"""
nombreArchivo = "Luchadores.txt"

#Se encarga de hacer un respaldo de la información del archivo de los luchadores
#y regresa una lista con el siguiente formato para que las funciones de edición
#de información pudan opcuparla

"""
FORMATO DE LA LISTA

[renglón 1, renglon 2, ..., renglón n]
renglon n = [Nombre, Ataque, Defensa, Vida]

"""
def recuperarArchivo():
    archivo = open(nombreArchivo,'r')
    #Al utiliar readlines obtenemos que lectura es una lista donde cada elemento 
    #es un renglón del archivo, lo que incluiría los datos de un personaje
    lectura = archivo.readlines()
    archivo.close()
    elementos = []
    
    #Recorre la lista de lectura y en cada reptición elemento toma el valor de
    #uno de los elementos de lectura
    for elemento in lectura:
        #Lo que hace es que en la lista elementos convierte nuestra información
        #en una lista de listas, donde cada lista contiene la información de un
        #personaje y a su vez esa información se encuentra listada
        elementos.append(elemento.split(' '))
    
    #Recorremos a elementos e i tomará un valor numérico desde 0 hasta la longitud 
    #de elementos (número de renglones) con el fin de que funcione como un indice
    for i in range(len(elementos)):
        #Con el primer índice recorremos cada uno de los renglones del archivo
        #Con el segundo índice indicamos que tomamos el último (len(elementos[i]-1)
        #Esto se realiza con el fin de que en el último elemento donde se realiza un salto de línea 
        #se quite el carácter \n (salto de línea) y se sutituya por nada, para 
        #poder trabajar de mejor manera la lista en las funciones de edición
        elementos[i][len(elementos[i])-1] = elementos[i][len(elementos[i])-1].replace('\n','')
    #Regresa la información con el formato de lista predefinido
    return elementos

#Esta funcion se encarga de que la lista que contiene la información ya 
#modificada sea convertida otra vez a un formato de texto que podamos 
#guardar en el archivo y que esta conserve su formato preestablecido
def crearTexto(lista):
    texto = ''
    
    #Recorre la lista de la información que tiene el formato utilizado en la 
    #función de recuperarArchivo, e i funciona como indice para recorrer el arreglo
    #este primer indice podríamos decir que recorre los renglones
    for i in range(len(lista)):
        #Recorre cada elemento de los renglones de la informacion, j sirve como
        #índice para recorrer cada elemento del renglon
        for j in range(len(lista[i])):
            #Lo que hace es que cada elemento lo convierte en texto y por medio
            #de la concatenación lo va agregando siempre al final de la variable
            #texto, al final esta variable tendra toda la información con los
            #formatos de espacio y saltos de renglón
            texto += lista[i][j]
            
            #Pregunta si es el final del renglón
            if j < len(lista[i])-1:
                #Si no es el final del renglón separa este elemento del siguiente
                #con un espacio
                texto += ' '
            else:
                #Si es el final del renglón separa la información de lo que sigue
                #con un salto de línea, con la idea de que el siguiente renglón empiece
                #en una nueva línea
                texto += '\n'
    #Regresa el texto completo que se va a guardar en el archivo ya con el formato deseado
    return texto

#Esta función contiene todo el algoritmo para crear un nuevo personaje
def crearPersonaje(nombre, ataque, defensa, vida):
    
    #Manda llamar a la función recuperar archivo que nos regresa una lista de
    #listas con el formato especificado([[N, A, D, V],[N, A, D, V],...])
    listaArchivo = recuperarArchivo()
    
    #Busca renglón por renglón que no este repetido el nombre del personaje
    for renglon in listaArchivo:
        #Si el nombre (renglon[0]) está repetido imprime que se repitió y termina
        #la ejecución de la función
        if renglon[0] == nombre:
            print("Personaje repetido, no se puede guardar")
            return
    #Si no esta repetido continua atomáticamente esta sección y guarda
    #al final de la lista con los personajes anteriores al nuevo
    listaArchivo.append([nombre,ataque,defensa,vida])
    #Crea con la información actualizada el texto a guardar
    texto = crearTexto(listaArchivo)
    #Reescribe el archivo con la nueva información
    archivo = open(nombreArchivo, 'w')
    archivo.write(texto)
    archivo.close()
    
#Esta función se encarga de editar algún personaje    
def editarPersonaje(nombre, ataque, defensa, vida):
    #Manda llamar a la función recuperar archivo que nos regresa una lista de
    #listas con el formato especificado([[N, A, D, V],[N, A, D, V],...])
    listaArchivo = recuperarArchivo()
    #Es una variable de control que me permitira conocer en que lugar se encuentra
    #el valor que estoy buscando por NOMBRE
    indice = -1
    #Recorre cada renglón de la lista e i funciona como un índice para recorrer
    #cada elemento
    for i in range(len(listaArchivo)):
        #Pregunta si el nombre (listaArchivo[i][0]) es igual al que busco
        if listaArchivo[i][0] == nombre:
            #Si es cierto guarda el índice
            indice = i
    #Pregunta si no se modifico la variable de control
    if indice == -1:
        #Si el valor no cambio (sigue siendo -1) implica que no encontró un 
        #nombre que coincida con el personaje buscado por lo cual termina la 
        #función, haciendoselo saber al usuario
        print("No se encuentra personaje")
        return
    
    #Si encontro una coincidencia entonces módifica el renglón en el que encontro
    #el nombre ([índice]) y actualiza la información
    listaArchivo[indice][1] = ataque
    listaArchivo[indice][2] = defensa
    listaArchivo[indice][3] = vida
    #Crea con la información actualizada el texto a guardar
    texto = crearTexto(listaArchivo)
    #Reescribe el archivo con la nueva información
    archivo = open(nombreArchivo, 'w')
    archivo.write(texto)
    archivo.close()
    
def borrarPersonaje(nombre):
    #Manda llamar a la función recuperar archivo que nos regresa una lista de
    #listas con el formato especificado([[N, A, D, V],[N, A, D, V],...])
    listaArchivo = recuperarArchivo()
    #Es una variable de control que me permitira conocer en que lugar se encuentra
    #el valor que estoy buscando por NOMBRE
    indice = -1
    #Recorre cada renglón de la lista e i funciona como un índice para recorrer
    #cada elemento
    for i in range(len(listaArchivo)):
        #Pregunta si el nombre (listaArchivo[i][0]) es igual al que busco
        if listaArchivo[i][0] == nombre:
            #Si es cierto guarda el índice
            indice = i
    #Pregunta si no se modifico la variable de control
    if indice == -1:
         #Si el valor no cambio (sigue siendo -1) implica que no encontró un 
        #nombre que coincida con el personaje buscado por lo cual termina la 
        #función, haciendoselo saber al usuario
        print("No se encuentra personaje")
        return
    #Remoueve de la lista el elemento correspindiente al índice[listaArchivo[indice]]
    listaArchivo.remove(listaArchivo[indice])
    #Crea con la información actualizada el texto a guardar
    texto = crearTexto(listaArchivo)
    #Reescribe el archivo con la nueva información
    archivo = open(nombreArchivo, 'w')
    archivo.write(texto)
    archivo.close() 