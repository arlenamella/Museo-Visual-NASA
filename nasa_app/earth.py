from modulo import get_nasa
import data as d
from datetime import date, timedelta

fecha_ayer = str(date.today() - timedelta(days = 1))  #timedelta cuenta la cantida de dias que quiero restar
    
def extraer_earth(fecha = fecha_ayer, api = d.API_KEY):
    y, m, d = fecha.split('-') #se utiliza el split para separar segun los guiones, para esto se debe declarar string en fecha_ayer, para que reconozca el split
    # y, m, d se utiliza para desempaquetar la lista que se genera con fecha.split

    url1 = f'https://api.nasa.gov/EPIC/api/natural/date/{fecha}?api_key={api}'
    get_url1 = get_nasa(url1)

    foto_id = [elemento['image'] for elemento in get_url1] #se genera la lista con las fotos
    tiempo = [elemento['date'] for elemento in get_url1] #se genera lista con la fecha

    url2 = f'https://api.nasa.gov/EPIC/archive/natural/{y}{m}{d}/png/'
    end = f'.png?api_key={api}'

    return [url2 + id + end for id in foto_id], tiempo

if __name__ == '__main__':
    print(fecha_ayer)
    fotos, horas = extraer_earth()
    print(fotos)
    print(horas)