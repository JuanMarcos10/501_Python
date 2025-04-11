# INPUT
nombre = input("Introduzca su nombre: ")

print("Bienvenido", nombre)

"""   IMPORTANTE: Todo lo introducido por input() se considera string, aunque sea un número, 
por lo que, si necesitamos operar matemáticamente con números, tendremos que hacer un casting: 
"""

edad = int(input("Introduzca su edad: "))
print("Bienvenido", nombre)
print("Tiene", edad, "años")

