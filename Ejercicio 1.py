#En el siguiente programa se visualizara si un número es primo o no
import math

numero = int(input('Ingrese un número: '))

def es_primo():
    if numero < 2:
        print('El número no es primo')
        return
    else:
        raiz_cuadrada = math.sqrt(numero)
        raiz_entero = math.floor(raiz_cuadrada)    
        
        for i in range(2, raiz_entero + 1):
            resto = numero % i
            
            if resto == 0:
                print('El número no es primo')
                return
    
    print('El número es primo')

es_primo()