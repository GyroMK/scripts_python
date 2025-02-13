import requests

def buscar_waifus(nombre_waifu):
    url = f"https://waifu.im/api/v1/search?q={nombre_waifu.replace(' ', '+')}"
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        return datos['results']
    else:
        return None

def mostrar_info_waifus(waifus):
    if waifus:
        for waifu in waifus:
            nombre = waifu['name']
            imagen = waifu['image']
            
            print(f"Nombre: {nombre}")
            print(f"Imagen: {imagen}")
    else:
        print("No se encontraron waifus.")

if __name__ == "__main__":
    nombre_waifu = input("Introduce el nombre de la waifu: ")
    waifus = buscar_waifus(nombre_waifu)
    mostrar_info_waifus(waifus)
