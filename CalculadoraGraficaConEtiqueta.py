# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 21:20:31 2020

@author: yocoy
"""

from tkinter import *

def sumar():
	try:
		num1 = int(numero1.get())
		num2 = int(numero2.get())

		result = str(num1+num2)
		resultado.config(text = "Resultado: " + result)
        
	except ValueError:
		messagebox.showinfo(message = "Error los números introducidos son inválidos", title = "ERROR 400")

def multiplicar():
	try:
		num1 = int(numero1.get())
		num2 = int(numero2.get())

		result = str(num1*num2)
		resultado.config(text = "Resultado: " + result)

	except ValueError:
		messagebox.showinfo(message = "Error los números introducidos son inválidos", title = "ERROR 400")
	
def restar():
	try:
		num1 = int(numero1.get())
		num2 = int(numero2.get())

		result = str(num1-num2)
		resultado.config(text = "Resultado: " + result)

	except ValueError:
		messagebox.showinfo(message = "Error los números introducidos son inválidos", title = "ERROR 400")

def dividir():
	try:
		num1 = int(numero1.get())
		num2 = int(numero2.get())

		result = str(num1/num2)
		resultado.config(text = "Resultado: " + result)


	except ValueError:
		messagebox.showinfo(message = "Error los números introducidos son inválidos", title = "ERROR 400")

	except ZeroDivisionError:
		messagebox.showinfo(message = "No se puede dividir entre 0", title = "ERROR 405")

ventana = Tk()

frame = Frame(ventana)
frame.pack(padx = 50, pady = 50)

etiqueta1 = Label(frame, text = "Número 1:")
etiqueta1.pack()

numero1 = Entry(frame)
numero1.pack()

etiqueta2 = Label(frame, text = "Número 2:")
etiqueta2.pack()

numero2 = Entry(frame)
numero2.pack()

boton_suma = Button(frame, text = "Sumar", command = sumar)
boton_suma.pack(side = LEFT)

boton_resta = Button(frame, text = "Restar", command = restar)
boton_resta.pack(side = LEFT)

boton_multiplicar = Button(frame, text = "Multiplicar", command = multiplicar)
boton_multiplicar.pack(side = LEFT)

boton_division = Button(frame, text = "Dividir", command = dividir)
boton_division.pack(side = LEFT)

resultado = Label(frame, text = "Resultado: ")
resultado.pack(side = TOP, before = etiqueta1)


ventana.mainloop()