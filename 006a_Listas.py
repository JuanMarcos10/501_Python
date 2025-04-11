#   LISTAS
"""
La lista es un tipo de colección ordenada y modificable. Se escriben entre corchetes. []
"""
miLista=["Hola", 43, "Esto es una lista", True]  # Ejemplo de lista

#   Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0]) # 22
print(miLista[1]) # True
print(miLista[3][1]) # 2
print(miLista[-2]) # "una cadena"
print(miLista[1:3]) # [True, 'una cadena']
print(miLista[:3]) # [22, True, 'una cadena']
print(miLista[2:]) # ['una cadena', [1, 2]]

#   MÉTODOS DE LAS LISTAS
#   Hacer una lista de una cadena
print(len(miLista)) # Imprime la longitud de la lista: 4
python_lista = list("PYTHON") # CREADOR DE LISTA: ['P', 'Y', 'T', 'H', 'O', 'N']

# Ver si un elemento está en la lista
if "H" in python_lista:
    print("La letra H está en la lista")
else:
    print("La letra H no está en la lista")

# Cambiar un elemento de la lista
python_lista[0] = "X" # Cambia el primer elemento de la lista por "X"

# Cambia un rando de la lista
python_lista[1:3] = ["E", "F"] # Cambia el segundo y tercer elemento de la lista por "Y" y "T"
print(python_lista) # ['X', 'E', 'F', 'H', 'O', 'N']

# Inserta un elemento en la lista
python_lista.insert(2, "Z") # Inserta "Z" en la posición 2 de la lista
print(python_lista) # ['X', 'E', 'Z', 'F', 'H', 'O', 'N']

# Añade un elemento al final de la lista
python_lista.append("A") # Añade "A" al final de la lista
print(python_lista) # ['X', 'E', 'Z', 'F', 'H', 'O', 'N', 'A']

# Extiende una lista con otra lista
python_lista.extend(["B", "C"]) # Añade "B" y "C" al final de la lista
print(python_lista) # ['X', 'E', 'Z', 'F', 'H', 'O', 'N', 'A', 'B', 'C']

# Elimina un elemento de la lista
python_lista.remove("E") # Elimina "Z" de la lista (si existe y la primera vez que lo encuenta) --> Si no encuentra el elemento, lanza un error - CUIDADO!
python_lista.pop()
print(python_lista) # ['X', 'Z', 'F', 'H', 'O', 'N', 'A', 'B', 'C']
del python_lista[3] # Elimina el elemento en la posición 8 de la lista
del python_lista # Elimina toda la lista --> # NameError: name 'python_lista' is not defined
python_lista = list("PYTHON") 
python_lista.clear() # Elimina todos los elementos de la lista pero la lista queda vacia []

# ITERACION EN UNA LISTA
lista = ['Manzana', 'Platano', 'Fresa']
for x in lista:
    print(x) # Imprime cada elemento de la lista en una línea diferente

# Misma iteración pero usando enumerate
for i, x in enumerate(lista):
    print(x) # Imprime cada elemento de la lista en una línea diferente

# Misma iteración pero usando range
for i in range(len(lista)):
    print(lista[i]) # Imprime cada elemento de la lista en una línea diferente

# Misma iteracion con comprehension de listas
[print(x) for x in lista] # Crea una nueva lista con los mismos elementos que la original

# Ordenar listas
lista.sort()
print(lista)

# Copiar listas
lista2 = lista.copy() # Copia la lista original en una nueva lista

lista3 = list(lista2) # Copia la lista original en una nueva lista

# Juntar listas
listas_juntadas = lista + lista2 + lista3
print(listas_juntadas)

lista4 = lista2.extend(lista) # Junta la lista original con la nueva lista y la guarda en la nueva lista 
"""
RESUMEN DE LOS MÉTODOS DE LISTAS:
append()  Añade un elemento al final de la lista
del       Elimina un elemento de la lista (por índice) o bien la lista completa
clear()   Elimina todos los elementos de la lista
copy()    Devuelve una copia de la lista
count()   Devuelve el número de elementos con el valor especificado
extend()  Añadir los elementos de una lista (o cualquier iterable), al final de la lista actual
index()   Devuelve el índice del primer elemento con el valor especificado
insert()  Añade un elemento en la posición especificada
pop()     Elimina el elemento en la posición especificada
remove()  Elimina el elemento con el valor especificado
reverse() Invierte el orden de la lista
sort()    Ordena la lista
"""