def saludar(nombre):
    print (nombre)
    print ("Hola",nombre)
    print(f"Hola {nombre}, bienvenido al curso de python")


saludar("Alex")

#-------

def sumar():
    resultado = 4 + 9
    return resultado

total = sumar()
print(total)

#-------

def sumar(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

total = sumar(2,8)
print(total)

total = sumar(142,84)
print(total)

total = sumar(123,5518)
print(total)

#-------

def mostrar_frutas(lista_frutas):
    print(lista_frutas)

frutas = ["manzana","platano","durazno"]
mostrar_frutas(frutas)

#-------

def mostrar_frutas(lista_frutas):
    print("la fruta que hay es:")
    for fruta in lista_frutas:
        print(fruta)


frutas = ["manzana","platano","durazno"]
mostrar_frutas(frutas)
a