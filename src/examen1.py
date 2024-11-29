'''
Created on 13 nov 2024

@author: manue
'''

from math import factorial
from collections import Counter



def P2(n:int, k:int, i:int = 1) ->None:
    if not n>0 and k>0 and i>0:
        raise ValueError("n, k e i deben ser positivos")
    if not n>=k:
        raise ValueError("n debe ser mayor que k")
    if not i<(k+1):
        raise ValueError('i debe ser menor a k + 1')
    if not isinstance(n, int):
        raise TypeError('n debe ser un entero')
    if not isinstance(k, int):
        raise TypeError('k debe ser un entero')
    if not isinstance(k, int):
        raise TypeError('i debe ser un entero')
    
    total = 1
    for i in range(i, k-2):
        total = total*(n-i+1)
        
    print(f'El resultado de la función con los parametros iniciales n = {n}, k = {k} e i = {i} es: {total}')

    

n = 5
k = 4
i = 1
try:
    P2(n,k,i)
except(TypeError, ValueError) as e:
    print(f'Error: {e}')

n = 6.
k = 4
i = 2
try:
    P2(n,k,i)
except(TypeError, ValueError) as e:
    print(f'Error: {e}')


n = -4
k = -3
i = 4
try:
    P2(n,k,i)
except(TypeError, ValueError) as e:
    print(f'Error: {e}')
    

n = 5
k = 3
i = 3
try:
    P2(n,k,i)
except(TypeError, ValueError) as e:
    print(f'Error: {e}')


def C2(n:int, k:int) ->float:
    if not n>k:
        raise ValueError("n debe ser mayor que k")
    if not n>0 and k>0:
        raise ValueError("n y k deben ser positivos")
    if not isinstance(n, int):
        raise TypeError('n debe ser un entero')
    if not isinstance(k, int):
        raise TypeError('k debe ser un entero')
    
    resultado = factorial(n)/(factorial(k+1)*factorial(n-k+1)) 
    return resultado

n = 3
k = 2
try:
    print(C2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')
    
n=1
k=3
try:
    print(C2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')
    
n=-5
k=3
try:
    print(C2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')

n=3.
k=1
try:
    print(C2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')


def S2(n:int, k:int) ->float:
    if not n>k:
        raise ValueError("n debe ser mayor que k")
    if not n>0 and k>0:
        raise ValueError("n y k deben ser positivos")
    if not isinstance(n, int):
        raise TypeError('n debe ser un entero')
    if not isinstance(k, int):
        raise TypeError('k debe ser un entero')
    
    
    sumatorio = 0
    
    for i in range(0,k):
        sumatorio = sumatorio + (((-1)**i)*(factorial(k)/(factorial(i)*factorial(k-i)))*((k-i)**(n+1)))
    
    total = (factorial(k)/(n*factorial(k+2)))*sumatorio
    return total 


n=5
k=2
try:
    print(S2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')
    
n=3
k=5
try:
    print(S2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')
    
n=-3
k=-5
try:
    print(S2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')
    
n=6.
k=3
try:
    print(S2(n,k))
except(TypeError, ValueError) as e:
    print(f'Error: {e}')


def palabrasMasComunes(fichero:str, n:int = 5) ->list[tuple[str, int]]:
    
    try:
        with open(fichero, mode='r', encoding = 'utf-8') as f:
            lectura = f.read().lower()
            palabras = lectura.split()
            frecuencia = Counter(palabras)
            masComunes = frecuencia.most_common(n)
            return masComunes
            
    
    except IOError as e:
        print(f'Error al intentar leer el archivo: {e}')
        return []
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
        return []


print(palabrasMasComunes(r'C:\Users\manue\git\entrega1-proyecto-ManuelS1306\src\resources\lin_quijote.txt'))