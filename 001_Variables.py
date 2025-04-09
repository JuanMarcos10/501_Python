# TIPO DE VARIABLES

# Declaración de variable NUMERICA ENTERA:
numero_entero = 23                     
print (numero_entero)

# Declaración de variable NUMERICA FLOTANTE
numero_flotante = -23.52            
print (numero_flotante)

# Declaración de variable de tipo string:
variable_string = 'Soy una frase en una línea'  
print (variable_string)

# Declaración de variable de tipo string en varias líneas:
s_textoLargo = """Esto es un mensaje    
...con tres saltos
...de linea"""
print(s_textoLargo)

# Sobreescribimos el valor de la variable s_edad y ahora la ponemos como string:
# numero_entero = "23"
# print (numero_entero)

# Declaración de constante:
NUMEROPI = 3.14159
print(NUMEROPI)

# Declaración de un boolean
is_verdadero = True
is_casado = False

# True = 1 y False = 0
True == 1
False == 0
print(True)

# Cuando se valida una condición , Python devuelve True o False:
print(1 > 2)
print(1 == 1)
print(1 < 2)

# Declaración múltiple
# En una sola instrucción, estamos declarando tres variables: a, b y c, 
a, b, c = 'string', 15, True
print(a, b, c)

# Para verificar el tipo de cualquier objeto en Python, usamos la función type():
print(numero_entero, ":", type(numero_entero))
print(numero_flotante, ":", type(numero_flotante))
print(NUMEROPI, ":", type(NUMEROPI)) # La anotacion de tipo MAYUSCULA es una convención para indicar que es una constante.
print(variable_string, ":", type(variable_string))
print(is_verdadero, ":", type(is_verdadero))
print(type(None))  

# Si queremos especificar el tipo de una variable, utilizamos casting:
entero = int(23.5)              # Convierte el número 23.5 a entero, es decir, 23
letras = str(23)                # Convierte el número 23 a string, es decir, '23'
flotante = float(23)            # Convierte el número 23 a flotante, es decir, 23.0
print(entero, ":", type(entero))
print(letras, ":", type(letras))
print(flotante, ":", type(flotante))

# Tipo complejo:
tipo_complex = 1j
print(tipo_complex, ":", type(tipo_complex))

# Tipo de lista
lista = ["a", "b", "c"]
print(lista, ":", type(lista))

# Tipo de tupla
tupla = ("a", "b", "c")
print(tupla, ":", type(tupla))

# Tipo de conjunto
conjunto = {"nombre", "edad"}
print(conjunto, ":", type(conjunto))

# Tipo de diccionario
diccionario = {"nombre": "Juan", "edad": 23}
print(diccionario, ":", type(diccionario))





