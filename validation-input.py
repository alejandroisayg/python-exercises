name = input("Cual es tu nombre?")
age = int(input("Cual es tu edad?"))

print ()

if age < 5:
    print(f"Lo siento {name}, los ninios menores de 5 anios no pueden entrar al cine.")
elif age <= 17:
    print(f"{name} Tu boleto cuesta $50 (Precio para ninios y adolescentes).")
elif age <60:
    print(f"{name} Tu boleto cuesta $100 (Precio para adultos).")
else:
    print(f"{name} Tu boleto cuesta $50 (Precio para adultos mayores).")