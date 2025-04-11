#   DICCIONARIOS
"""Un diccionario es una colección desordenada, modificable e indexada, se escriben entre llaves y tienen claves y valores.
"""
#   Declaración de un diccionario
persona = {
    "Nombre": 'Juan',
    "Edad": 30,
    "Ciudad": "España"
}
print(persona["Nombre"]) # Juan
persona["Edad"] = 35 # Cambia el valor de la clave "Edad" a 35
persona["Profesion"] = "Ingeniero" # Agrega una nueva clave "Profesion" con el valor "Ingeniero"

for clave, valor in persona.items():
    print(clave, ": ", valor)
"""
Nombre :  Juan
Edad :  35
Ciudad :  España
Profesion :  Ingeniero
"""
#   Imprima las claves del diccionario:
for x in persona:
      print(persona[x]) # Juan, 35, España

#   Quitar valores de un diccionario
persona.pop("Profesion")	# {'Nombre': 'Juan', 'Edad': 35, 'Ciudad': 'España'}

#   Crear un diccionario a partir de dos listas:
lista_claves=["nombre", "edad"]
lista_valores=["Jesus", 33]
diccionario = dict(zip(lista_claves , lista_valores)) # {'nombre': 'Jesus', 'edad': 33}

#   Para comprobar si una clave está en el diccionario:
print("nombre" in diccionario)		# Devuelve true o false (En este caso True)

#   Copiar un diccionario
persona2 = persona.copy() # {'Nombre': 'Juan', 'Edad': 35, 'Ciudad': 'España'}

#   Otra forma de copiar un diccionario
persona3 = dict(persona2) # {'Nombre': 'Juan', 'Edad': 35, 'Ciudad': 'España'}

#   Longitud de un diccionario:
print(len(persona)) # 3

#   Eliminar el último elemento insertado:
persona3.popitem() # {'Nombre': 'Juan', 'Edad': 35}
print(persona3) 

#   La palabra clave del elimina el elemento con el nombre de clave especificado:
del persona3["Edad"] # {'Nombre': 'Juan'}

#   La palabra clave clear() vacía el diccionario:
persona3.clear() # {}

#   La palabra clave del también puede eliminar completamente el diccionario:
del persona2
      


