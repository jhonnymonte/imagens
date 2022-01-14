import requests
from bs4 import BeautifulSoup
import os
import time
# URL Hardcodeada para hacerlo mas rapido
url = "https://www.fortnitecountdown.com/tienda/actual/"


def create_folder(path):
    ''' la funcion crea las carpetas de forma automatica y notifica la creacion de los mismos
    '''
    try:
        file_path = os.getcwd() + path
        print(file_path)
        # Determinar si el directorio ya existe
        if not os.path.exists(file_path):
            # El directorio no existe, crea la operación
            # Utilice el método os.makedirs () para crear directorios de niveles múltiples
            os.makedirs(file_path)
            print("Directorio creado con éxito:" + file_path)
        else:
            print("¡El directorio ya existe!")
    except BaseException as msg:
        print("Error al crear el nuevo directorio:" + msg)


def fetch(url, type):
    ''' la funcion invoca a la funcion create folder y crea carpeta correspondiente con nombre por argumento
        la funcion toma 2 argumentos la url y un string para el nombre de la carpeta por ejemplo "fornite"
    '''

    with requests.Session() as s:
        folder = f"./{type}"
        create_folder(folder)
        # send get request


response = requests.get(url)

html_page = BeautifulSoup(response.text, 'html.parser')

images = html_page.find_all("img")

for index, image in enumerate(images):
    image_url = image.get("src")  # img src value

    # tomar la extension de la imagen
    image_extension = image_url.split(".")[-1]

    # get image data
    image_bytes = requests.get(image_url).content

    if image_bytes:
        # write the image data
        with open(f"Image {index+1}.{image_extension}", "wb") as file:
            file.write(image_bytes)
            print(f"Downloading image {index+1}.{image_extension}")
