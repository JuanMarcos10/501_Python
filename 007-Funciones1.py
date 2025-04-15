# FUNCION BASICA
def miFunción():
    print('Primero imprimo esto')
    print('Y despues la segunda línea')
miFunción()


# FUNCION CON ARGUMENTOS - SUMAR
# Definición de la función sumar
def sumar(a, b):
    resultado = a + b
    return resultado
# Introducción de datos
arg1 = float(input('Proporciona el argumento 1: '))
arg2 = float(input('Proporciona el argumento 2: '))
# Llamamos a la función sumar
resultado_suma = sumar(arg1, arg2)
print(f'Resultado suma: {resultado_suma}')

# FUNCION CON ARGUMENTOS Y RETORNANDO VARIOS DATOS
def obtener_coordenadas():
    x, y, z = 100, 200, 300
    return x, y, z
# Llamar la funcion
resultado = obtener_coordenadas()
print(resultado)
# Unpacking de la tupla
x1, y1, z1 = resultado
# Imprimir los valores de manera individual
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')

# FUNCION RECURSIVA - FACTORIAL
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
print(factorial(5))

# FUNCION RECURSIVA - IMPRIMIR DEL 1 AL 5
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ')
    else:  # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')
funcion_recursiva(5)

# FUNCION SUMAR QUE ACEPTA ARGUMENTOS VARIABLES
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total
# Llamamos a la funcion de sumar
resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8)
print(f'Resultado de la suma: {resultado}')

print('*** Usando kwargs para imprimir información ***')

# FUNCION QUE ACEPTA ARGUMENTOS VARIABLES DE TIPO LLAVE VALOR
def imprimir_info(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')
# Llamamos a la funcion
imprimir_info(nombre='Paula', edad=30, ciudad='Lugo')
imprimir_info(nombre='Carlos', edad=28, ciudad='Madrid', puesto='Gerente')