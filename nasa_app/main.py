from modulo_html import crear_html, crear_html_planeta, crear_html_rotacion
from validar import validate
from show import show_fotos
from apod import extraer_fotos
from planeta import extraer_planetas
from earth import extraer_earth

opciones= input('''Bienvenido al Museo Visual de la NASA: ¿Listo para aprender?
        ¿Qué desea ver?
        
        1. Foto del día
        2. Fotos de Planetas
        3. Ver la rotación de la Tierra en un día
        0. Salir
        ''') 

opciones = int(validate(['0','1','2','3'], opciones))

while True: #este es un menú infinito, por lo tanto se debe colocar una finalización
    if opciones == 1:
        n = int(input(''' En este módulo podrás ver la foto del día.
        Esta es una fot emblemática tomada por la Nasa.
        Por favor indica cuántas fotos quieres ver: 
        > '''))
        id_foto = extraer_fotos(n)
        html = crear_html(id_foto)
       #esto se sustituye por el show fotos 
       # with open('apod.html', 'w') as file:
        #    file.write(html)
        show_fotos(html, 'apod')
    elif opciones == 2:
        planeta = input('''En este módulo podrás ver fotos emblemáticas de planetas tomadas por la Nasa.
                            Por favor escoge un planeta:
                            1. Mercurio
                            2. Venus
                            3. Tierra
                            4. Marte
                            5. Jupiter
                            6. Saturno
                            7. Urano
                            8. Neptuno
                            > ''')
        planeta = int(validate(['1', '2', '3','4','5','6','7','8'],planeta))
        n = int(input('¿Cuántas fotos quieres ver? '))
        titulos, descripcion, fotos = extraer_planetas(planeta, n)  #esta parte hay que pasarla al modulo html
        html = crear_html_planeta(titulos, descripcion, fotos)
        show_fotos(html, 'planetas')
    
    elif opciones == 3:
        fecha = input('''En este módulo podrás ver fotos emblemáticas que muestran la rotación de la tierra.
        Por favor escoge una fecha en la que desees ver la tierra. (máxima fecha: ayer)
        Formato: YYYY-MM-DD
        > ''')
        fotos, horas = extraer_earth(fecha)
        html = crear_html_rotacion(fotos, horas)
        show_fotos(html, 'rotacion')
    else:
        exit() #para finalizar el ciclo

#se debe crear un modulo para validar las opciones, en caso de que la persona ingrese un menú invalido