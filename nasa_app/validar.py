

def validate(opciones, elecciones):
    while elecciones not in opciones:
        elecciones = input('Has ingresado una opción incorrecta: Por favor escoje una de las opciones disponibles: ')

    return elecciones

if __name__ == '__main__':
    opciones = ['1','2','3','0']
    elecciones = input('Escoja una opción: ')
    validate(opciones,elecciones)