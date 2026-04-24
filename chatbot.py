import requests

API_KEY = 'sk-ad39d94aa5af4f1999022622d4610008'

url = 'http://api.deepseek.com/chat/completions'

header = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print ("Con que personaje quieres platicar?")
print ("A) Bob Esponja")
print ("B) Leslie Knope de Parks and Recreation")
print ("C) Ramona Flowers de Scott Pilgrim vs The World")

option = input("Elige A, B o C:").lower()

if option == 'a':
    personaje = "Bob Esponja"
elif option == 'b':
    personaje = "Leslie Knope de Parks and Recreation"
elif option == 'c':
    personaje = "Ramona Flowers de Scott Pilgrim vs The World"
else:
    print ("opcion no valida")
    exit()

mensaje = [
    {
        "role": "system",
        "content": f"Actua como si fueras {personaje}. Presentate primero y luego responde siempre como ese personaje"
    }
]

data = {
    "model": "deepseek-chat",
    "messages": mensaje
}
response = requests.post(url, headers=header, json=data)

if response.status_code == 200:
    respuesta = response.json()
    contenido = respuesta['choices'][0]['message']['content']
    print("\n" + contenido)
    mensaje.append({"role":"assistant","content": contenido})
else:
    print(f"Error al comunicar con la API (status {response.status_code})")
    print(response.text)
    exit()