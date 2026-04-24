"""
nombre = "Alex"
print ("Hola", nombre)

edad = 29
print ("Tienes", edad)


edad_usuario = int(input("Cuatos años tienes? "))
print ("La edad del usuario es:", edad_usuario)

if edad_usuario >= 17:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
"""

frutas = ["Manzana", "Pera", "Naranja"]

print("Fruta 1:", frutas[2])

for fruta in frutas:
    print("Fruta", fruta)

print(len(frutas))

frutas.append("Uva")

print(len(frutas))