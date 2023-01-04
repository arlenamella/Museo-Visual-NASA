import requests
import json
import random
from data import API_KEY
from modulo import get_nasa #esto se agrega despues que se crea el archivo modulo

def extraer_fotos(n, total = 50, api = API_KEY):
    url = f' https://api.nasa.gov/planetary/apod?count={total}&api_key={api}'
   # resultado = json.loads(requests.get(url).text)  #esto se repite en el archivo planeta.py por lo tanto lo vamos a modularizar en un archivo que se llamará modulo.py
    resultado = get_nasa(url) #esto se agrega para sustituir la linea de arriba, luego de hacer el archivo de modularización
    galeria_fotos = [elemento for elemento in resultado if elemento['media_type']=='image']

    return random.choices(galeria_fotos, k = n)

if __name__ == '__main__':
    print(extraer_fotos(2))