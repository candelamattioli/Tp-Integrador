import math

def cuadratica(a, b, c):
    raiz_cuadrada = math.sqrt(math.pow(b, 2) - 4 * a * c)
    resultado_a = (-b + raiz_cuadrada) / (2 * a)
    resultado_b = (-b - raiz_cuadrada) / (2 * a)
    
    print(f'El resultado a es: {resultado_a}')
    print(f'El resultado b es: {resultado_b}')
    
a = int(input('Ingrese valor de a: '))
b = int(input('Ingrese valor de b: '))
c = int(input('Ingrese valor de c: '))

cuadratica(a, b, c)
