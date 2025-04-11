#   TUPLAS
"""Una tupla es una colección ordenada e inmutable. Entre paréntesis. ()
"""
#       Declaración de una tupla
miTupla = ("manzana", "banana", "cereza")

#   Otra forma de declararla
miTupla = tuple(("manzana", "banana", "cereza"))

#   Convierta la tupla en una lista para poder cambiarla:
miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
print(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)
print(miTupla) 

#   Recorrer una tupla
miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
  print(x)

#   Comprobar si existe un elemento
miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
  print("Sí, 'manzana' está en la tupla.")
#   Otra forma, simplemente con un boolean
print("manzana" in miTupla) 

#   Longitud de la tupla
miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))

# Unir dos tuplas
tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

#   Cuantas veces se encuentra el "manzana" en miTupla?
miTupla = ("manzana", "banana", "cereza" , "manzana")
print(miTupla.count("manzana"))	

#   Desempaquetdo de tupla
valor1, valor2, valor3, valor4 = miTupla
print(valor1, valor2, valor3, valor4) # manzana banana cereza manzana








