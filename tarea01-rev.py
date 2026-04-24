def caja_registradora():
    productos = []

    for i in range(3):
            elproducto = input("Ingrese el nombre del producto: ")
            productos.append(elproducto)

    for product in productos:
        print (f"El producto registrado es {product}")

    print(productos)

caja_registradora()

#.pop = para borrar/eliminar algo, quita la posicion
#.remove = borra un elemento que se repite, quita todas las iteraciones