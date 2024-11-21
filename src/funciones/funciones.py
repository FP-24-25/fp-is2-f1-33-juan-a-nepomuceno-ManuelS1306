'''
Created on 13 nov 2024

@author: manue
'''

import math


def productoSerie(n:int, k:int) ->None:
    
    if n<= k:
        raise ValueError('n debe ser mayor que k')
    
    total:int = 1
    for i in range(k):
        total = total*(n-i+1)
        
    print(f'El producto de {n} y {k} es: {total}')
    
    

def sucesionGeometrica(a1:int, k:int, r:int) -> None:
    
    total:int = 1
    for n in range(1, k+1):
        termino:int = a1 * (r ** (n-1))
        total *=termino
        
    print(f'El producto de la secuencia geométrica con a1 = {a1}, r = {r} y k = {k} es: {total}')


def numeroCombinatorio(n:int, k:int) -> None:
    
    if n<= k:
        raise ValueError('n debe ser mayor que k')
        
    subconjuntos:float = ((math.factorial(n))/(math.factorial(k)*math.factorial(n-k))) #Fórmula del número combinatorio
       
    print(f'El número combinatorio de {n} y {k} es: {subconjuntos}')

def sumatorio(n:int, k:int) ->None:
    
    if n<= k:
        raise ValueError('n debe ser mayor que k')
    
    sumatorio:int = 0
    for i in range(0,k):
        sumatorio = sumatorio + ((-1)**i)*((math.factorial(k+1))/(math.factorial(i+1)*math.factorial((k+1)-(i+1))))*((k-i)**n)
    total:float = (1/(math.factorial(k)))*sumatorio
    
    print(f'El número S(n,k) siendo n = {n} y k = {k} es: {total}')


def metodoNewton(f, f_derivada, a:float, e:float) ->float:
    
    xn:float = a
    
    while abs(f(xn)) > e:
        try:
            
            xn = xn - (f(xn)/f_derivada(xn))
            
        except ZeroDivisionError:
            print(f'La derivada se anula en: {xn}')
    
    return xn