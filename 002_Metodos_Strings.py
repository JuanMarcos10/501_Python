#   MÉTODOS DE LOS STRINGS:

#   lower(): Convierte en minúsculas un string.
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print(s_texto1.lower()) # Resultado: este texto está inicialmente en mayúsculas

#   capitalize(): Pone la primera letra en mayúscula.
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print(s_texto2.capitalize()) # Resultado: Este texto no tenía la primera letra en mayúsculas

#   count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print(s_texto3.count('c')) # 4

#   find(): Representa el índice o la posición en el cual aparece un carácter o un grupo de caracteres. Si aparece varias veces me dice sólo el primero.
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print(s_texto4.find('e')) # 9
# NOTA: Si no encuentra el carácter o la cadena de caracteres devuelve -1.

#   rfind(): Igual que find() pero cuenta la última encontrada.
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto5.rfind('desde')) # 63 --> En la posición 63 aparece la última vez la palabra desde.
print(s_texto5.find('desde')) # 47 --> En la posición 47 aparece la primera vez la palabra desde.

#   isdigit(): Devuelve un boolean, nos dice si el valor introducido es un string. Tiene que ser un valor introducido entre comillas o dará error.
s_texto6 = "6"
print(s_texto6.isdigit()) # True

#   isalum(): Devuelve un boolean, Devuelve verdadero si todos los caracteres de la cadena son numéricos y hay al menos un carácter. En caso contrario, devuelve falso.
s_texto7 = "9857654gf7" 
print(s_texto7.isalnum()) # True

#   isalpha(): Devuelve un boolean, comprueba si hay sólo letras. Los espacios no cuentan.
s_texto8 = "Holamundo"
print(s_texto8.isalpha()) #True

#   split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split()) # ['Vamos', 'a', 'separar', 'esta', 'frase', 'por', 'los', 'espacios']

#   Podemos usar otro carácter como separador, por ejemplo una coma:
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print(s_texto10.split(",")) # ['Esta sería la primera parte', 'y esta la segunda']
 
#   strip(): Borra los espacios sobrantes al principio y al final.
s_texto11 = "   En este texto había espacios al principio y al final    "
print(s_texto11.strip()) # 'En este texto había espacios al principio y al final'

#  replace(). Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
miString = "Esto es bonito. Esto es bueno."
newString = miString.replace("es" ,"FUE") # Esto FUE bonito. Esto FUE bueno.

#   Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b		 # c es "unodos"
c = a * 3 		 # c es "unounouno"

# Concatenacion de Cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + ' ' + cadena2
print(concatenacion) # Hola Mundo

# Utilizando el metodo str.join
concatenacion = "".join([cadena1,' ',cadena2])
print(concatenacion) # Hola Mundo

# Formato Cadenas
nombre = 'Juan'
edad = 30
mensaje = 'Hola, me llamo {} y tengo {} años.'.format(nombre, edad)
print(mensaje) # Hola, me llamo Juan y tengo 30 años.

# f-strings
mensaje = (f'Hola, me llamo {nombre} y tengo {edad} años.')
print(mensaje) # Hola, me llamo Juan y tengo 30 años.

# Manejo de subcadenas
cadena = 'Hola, mundo!'

# Obtenemos la subcadena de Hola
subcadena1 = cadena[0:4]  # [inicio:fin(exclusivo)]
print(subcadena1) # Hola

# Obtener la subcadena de Mundo
subcadena2 = cadena[6:11]
print(subcadena2) # Mundo

import random

letras = list('abcdefghijkl')   # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']  

l1 = letras[0:5] # ['a', 'b', 'c', 'd', 'e']
l2 = letras[5:10] # ['f', 'g', 'h', 'i', 'j']
random.shuffle(l1) # Mezcla la lista l1
print(l1) # ejemplo: ['d', 'b', 'e', 'c', 'a']

for a, b in zip(l1, l2): # la función zip() combina dos listas en una sola
    print(a + b, end=" ")

vocales = list("aeiou") # ['a', 'e', 'i', 'o', 'u'] 
for i in range(len(letras)):
    if letras[i] in vocales:
        print('{} en la posición {}'.format(letras[i], i))

for i, letra in enumerate(letras): # enumerate() devuelve un objeto iterable que contiene pares de índice y valor
    if letra in vocales:
        print('{} en la posición {}'.format(letra, i))
        
abcde = sorted(letras)[:7]
print(abcde)
print(list(enumerate(abcde)))
print(list(enumerate(abcde, 11)))