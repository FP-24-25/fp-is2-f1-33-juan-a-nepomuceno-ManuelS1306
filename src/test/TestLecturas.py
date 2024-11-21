'''
Created on 13 nov 2024

@author: manue
'''

from lecturas.lecturas import numRepeticiones, repeticionesCadena, palabras_unicas, longitud_promedio_lineas

fichero1:str = r'C:\Users\manue\git\entrega1-proyecto-ManuelS1306\src\resources\lin_quijote.txt'
fichero2:str = r'C:\Users\manue\git\entrega1-proyecto-ManuelS1306\src\resources\archivo_palabras.txt'
fichero3:str = r'C:\Users\manue\git\entrega1-proyecto-ManuelS1306\src\resources\palabras_random.csv'
cad:str = 'quijote'
sep:str = ' '
longitud_media = longitud_promedio_lineas(fichero3)

#Función 6

print('Test de la función 6:')
numRepeticiones(fichero1, cad, sep)

#Función 7

print('Test de la función 7:')
repeticionesCadena(fichero1, cad)

#Función 8

print('Test de la función 8:')
palabras_unicas(fichero2)

#Función 9

print('Test de la función 9:')
print(f'La longitud promedio de las líneas del fichero {fichero3} es: {longitud_media}')