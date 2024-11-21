'''
Created on 13 nov 2024

@author: manue
'''

import csv
from typing import Optional


def numRepeticiones(fichero:str, cad:str, sep):
    
    repeticiones:int = 0
    
    try:
        
        with open(fichero, mode = 'r', encoding = 'utf-8') as f:
            
            lectura:str = f.read().lower()
            repeticiones = lectura.split(sep).count(cad.lower())
        
        print(f'El número de veces que aparece la palabra {cad} en el fichero {fichero} es: {repeticiones}')

    except IOError as e:
        print(f'Error al intentar leer el archivo: {e}')
        
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
        
        
def repeticionesCadena(fichero, cad:str):
    
    lineasCad:list[str] = []
    try:
        
        with open(fichero, mode = 'r', encoding = 'utf-8') as f:
            for linea in f:
                if cad.lower() in linea.lower():
                    lineasCad.append(linea.strip())
                
        print(f'Las líneas en las que aparece la palabra {cad} son: {lineasCad}')
    
    except IOError as e:
        print(f'Error al intentar leer el archivo: {e}')
        return []
        
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
        return []
        
        
def palabras_unicas(fichero):
    
    unicas = set()
    try:
        
        with open(fichero, mode = 'r', encoding = 'utf-8') as f:
            for linea in f:
                palabras:str = linea.lower().split()
                unicas.update(palabras)
                lista:list[str] = list(unicas)
        
        print(f'Las palabras únicas en el fichero {fichero} son: {lista}')
    
    except IOError as e:
        print(f'Error al intentar leer el archivo: {e}')
        
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
        
def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    
    try:
        with open(file_path, mode= 'r', encoding= 'utf-8') as archivo:
            
            lectura = csv.reader(archivo, delimiter = ",")
            total_lineas:int = 0
            total_palabras:int = 0
            for linea in lectura:
                total_palabras = total_palabras + len(linea)
                total_lineas = total_lineas + 1
            
            if total_lineas == 0:
                return None
            
            longitud_media:float = total_palabras/total_lineas
        
        return longitud_media
        
    except IOError as e:
        print(f'Error al intentar leer el archivo: {e}')
        return None
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
        return None