import requests

nombre = input("Ingrese el nombre de un pokemon: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

response = requests.get(url)

if response.status_code == 200:
    datos = response.json()

    print("===Informacion del Pokemon===")
    print("Nombre", datos['name'])
    print("ID", datos['id'])
    print("Altura", datos['height'])
    print("Peso", datos['weight'])
    print("Imagen", datos['sprites']['front_default'])
else:
    print("Pokemon no encontrado, dang looooseeeeer")