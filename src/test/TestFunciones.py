'''
Created on 13 nov 2024

@author: manue
'''

from funciones.funciones import productoSerie, sucesionGeometrica, numeroCombinatorio, sumatorio, metodoNewton

#Función 1
print('Test de la función 1:')
productoSerie(4, 2)

#Función 2
print('Test de la función 2:')
sucesionGeometrica(3, 2, 5)

#Función 3
print('Test de la función 3:')
numeroCombinatorio(4, 2)

#Función 4
print('Test de la funcion 4:')
sumatorio(4, 2)

#Función 5

def f(x):
    return 2 * x **2

def f_derivada(x):
    return 4 * x 
a:float = 3
e:float = 0.001

resultado:float = metodoNewton(f, f_derivada, a, e)

print('Test de la función 5:')
print(f"Resultado de la función 5 con a = {a} y e = {e}, f(x) = 2x^2 y f'(x) = 4x: {resultado}")