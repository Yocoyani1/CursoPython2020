# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:17:04 2020

@author: yocoy
"""

import serial, time 

arduino = serial.Serial("COM3", 9600)
time.sleep(4)

arduino.write(b'1')
    
lecturas = []
for i in range(100):
    lecturas.append(arduino.readline())


arduino.close()

print(lecturas)
print(str(lecturas[0]))