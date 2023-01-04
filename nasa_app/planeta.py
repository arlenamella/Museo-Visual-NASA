from modulo import get_nasa
import random

#se crea esta función auxiliar para extraer la ruta de la foto que necesitaremos mas abajo
def get_foto(url):
    return get_nasa(url)['collection']['items'][0]['href'] #lo que esta en los corchetes me da la ruta dentro de la api

def extraer_planetas(eleccion, n): # n es el número de fotos que se quieren extraer, y elección es la elección del usuario
    planetas = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'] #esta es la lista de donde se tomará el elemento elegido
    url = f'https://images-api.nasa.gov/search?q={planetas[eleccion-1]}'

   # resultado = json.loads(requests.get(url).text) #esto se repite en el archivo apod.py por lo tanto lo vamos a modularizar en un archivo que se llamará modulo.py
    resultado = get_nasa(url)['collection']['items'] #esto se agrega para sustituir la linea de arriba, luego de hacer el archivo de modularización
    elecciones = random.choices(resultado, k=n) #random hace que las fotos se seleccionen al azar

    #voy a crear list comprehension para extraer la información que queremos
    nasa_id = [elemento['data'][0]['nasa_id'] for elemento in elecciones] # se utiliza nad_id que es donde esta el id en la api
    descripcion = [elemento['data'][0]['description'] for elemento in elecciones]
    titulo = [elemento['data'][0]['title'] for elemento in elecciones]
    foto = [get_foto(f'https://images-api.nasa.gov/asset/{id}') for id in nasa_id] #aqui se hace un llamado a cada asset mediante la url, y se reemplaza el id
    
    return titulo, descripcion, foto 

if __name__ == '__main__':
    #print(extraer_planetas(2,3)) #2 es la posición del planeta que quiero ver y 3 es la cantidad de fotos
    lista_titulos, descripcion, lista_fotos = extraer_planetas(2,3)
    print(lista_titulos)
    print(descripcion)
    print(lista_fotos)
