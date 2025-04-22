#   -------------------------------------
#   FUNCIONES LAMBDA
#   -------------------------------------
# Es una función anónima (sin nombre) que puedes definir en una sola línea. 
# Ideal para usar como funciones cortas y rápidas, especialmente cuando las 

# Sintaxis: lambda argumentos: expresión

# Ejemplo básico
doble = lambda x: x * 2
print(doble(5))  # → 10
# Equivale a:
def doble(x):
    return x * 2

# 1. Con map() → aplicar una función a cada elemento de una lista
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # → [1, 4, 9, 16]

# 2. Con filter() → filtrar elementos que cumplan una condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # → [2, 4]

