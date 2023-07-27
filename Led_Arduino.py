# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 00:06:57 2023

@author: silas
"""


from pyfirmata import Arduino
import  PySimpleGUI as sg

try:
    arduino = Arduino('COM7') # Colocar a porta COM que seu Arduino utiliza
    led = arduino.get_pin('d:13:o')
except:
    print("Porta COM não encontrada")

sg.theme('DarkGrey3')
layout=[
        [sg.Text('Controle LED')],
        [sg.Button('Ligar', key='lig'),sg.Button('Desligar', key='desl')]
 ]

janela = sg.Window('Python com Arduino',layout, size=(300,200))

while True:
    evento, dado = janela.read()
    if evento == 'lig':
        led.write(1)
    elif evento == 'desl':
        led.write(0)
    elif evento == sg.WIN_CLOSED:
        break

janela.close()
