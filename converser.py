print ("===Conversor de divisas===")

print ("1- USD a MXN")
print ("2- MXN a USD")
print ("3- EUR a MXN")
print ("4- MXN a EUR")

cantidad = 0

option = int(input("Selecciona el tipo de cambio que quieres realizar 1-4"))

cantidad = float(input("Ingresa la cantidad que deseas convertir:"))

if option == 1:
    resultado = cantidad * 18.31
    print(f"{cantidad} USD son {resultado} MXN")
elif option == 2:
    resultado = cantidad / 18.31
    print(f"{cantidad} MXN son {resultado} USD")
elif option == 3:
    resultado = cantidad * 21.31
    print(f"{cantidad} EUR son {resultado} MXN")
elif option == 4:
    resultado = cantidad / 21.31
    print(f"{cantidad} MXN son {resultado} EUR")
else:
    print ("Opcion no valida. Seleccionar una opcion del 1 al 4.")

print (f"total de cambio: ${resultado}.")
print ("Gracias por utilizar nuestro servicio, que tenga buen dia.")

# USD a MXN 
resultado = cantidad * 18.31

# MXN a USD
resultado = cantidad / 18.31

# EUR a MXN
resultado = cantidad * 21.31

# MXN a EUR
resultado = cantidad / 21.31