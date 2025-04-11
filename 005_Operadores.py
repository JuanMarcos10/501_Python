# IFs y ELSEs
edad = int(input("Ingresa tu edad: "))

if edad <= 0:
    print("La edad no puede ser negativa.")
elif edad > 65:
    print("Eres mayor de edad y jubilado.")
elif edad >= 18: 
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")
    
# OPERADOR TERNARIO igual que el anterior pero con una sola condición en una sola línea
print("Eres mayor de edad." if int(input("Ingresa tu edad: ")) >= 18 else "No eres mayor de edad.")

# FOR
#  Imprime el contenido del diccionario
for i in ["primavera", "verano", "otoño", "invierno"]:		
	print(i)

for i in range(5):
    print(f"Valor de la variable {i}")

#   Bucle for anidado
#   Imprime cada color para cada fruta:
frutas = ["manzana", "banana", "cereza"]
color = ["verde", "amarilla", "roja"]
for x in frutas:
  for y in color:
    print(x, y)

#	WHILE
#   Imprime edad cuando el contador llegue a 18

while edad<0:
    print("Edad incorrecta")
    edad=int(input("Introduce edad: "))
print("tu edad es: "+str(edad))

#   Bucle while con un if anidado y un break
#   Salga del bucle cuando num sea 3:
num = 1
while num < 6:
  print(num)
  if num == 3:
    break
  num += 1