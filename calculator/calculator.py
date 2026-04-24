import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("300x400")


tk.Label(ventana, text="Numero 1:").pack()
entrada1 = tk.Entry(ventana, font=("Arial", 18))
entrada1.pack()

tk.Label(ventana, text="Numero 2:").pack()
entrada2 = tk.Entry(ventana, font=("Arial", 18))
entrada2.pack()

resultado = tk.Label(ventana, text="Resultado: ", font=("Arial",18), fg="blue")
resultado.pack(pady=20)

def calcular(operacion):
    a = float(entrada1.get())
    b = float(entrada2.get())
    
    if operacion == "+":
        res = a + b
    elif operacion == "-":
        res = a - b
    elif operacion == "*":
        res = a * b
    elif operacion == "/":
        res = a / b
    else:
        res = "Operacion no valida"

    resultado.config(text=f"Resultado: {res}")

def borrar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text="Resultado: ")

tk.Button(ventana, text="Sumar +", command=lambda: calcular("+")).pack()
tk.Button(ventana, text="Restar -", command=lambda: calcular("-")).pack()
tk.Button(ventana, text="Multiplicar *", command=lambda: calcular("*")).pack()
tk.Button(ventana, text="Dividir /", command=lambda: calcular("/")).pack()
tk.Button(ventana, text="Borrar", command= borrar).pack(pady=10)

ventana.mainloop()