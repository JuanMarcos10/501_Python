import math
import random

a = math.pi * 1 # Numero pi: 3.141592653589793
print(a)

print(math.sqrt(4)) # Funciones matemáticas - Raiz cuadrada
print( random.random()) # Genera un número aleatorio entre 0 y 1
print("{:.2f}".format(random.random())) # Formato de 2 decimales

lista = [1, 2, 3, 4, 5]
listaRandom = random.choice(lista) # Elige un elemento aleatorio de la lista

nums = range(10) # range(0, 10)
list_of_nums = list(nums)
print(list_of_nums)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in range(1, 6):
    print(_)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

