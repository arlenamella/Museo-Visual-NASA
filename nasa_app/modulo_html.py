

def crear_html(lista_diccionario):

    acum = '' #declaramos un acumulador vacío que llenaremos con el for
    for foto in lista_diccionario:
        acum += f'''<h1>{foto['title']}<h1>
        <p>{foto['date']}</p>
        <img src={foto['url']}>
        <p>{foto['explanation']}</p>
        '''

    html = f'''
    <html>
        <head>
        </head>
            <body>
            {acum}
            </body>
    </html>'''

    return html

def crear_html_planeta(lista_titulo, lista_descripciones, lista_fotos):

    acum = '' #declaramos un acumulador vacío que llenaremos con el for
    for lt, ld, lf in zip(lista_titulo, lista_descripciones, lista_fotos):
        acum += f'''<h1>{lt}<h1>
        <img src='{lf}' width='50%'>
        <p>{ld}</p>
        '''

    html = f'''
    <html>
        <head>
        </head>
            <body>
            {acum}
            </body>
    </html>'''

    return html


def crear_html_rotacion(lista_fotos, lista_horas):

    acum = '' #declaramos un acumulador vacío que llenaremos con el for
    for lf, lh in zip(lista_fotos, lista_horas):
        acum += f'''<p>{lh}<p>
        <img src='{lf}' width='50%'>
    
        '''

    html = f'''
    <html>
        <head>
        </head>
            <body>
            {acum}
            </body>
    </html>'''

    return html

if __name__ == '__main__':
    from apod import extraer_fotos
    from planeta import extraer_planetas
    from show import show_fotos
    from earth import extraer_earth

    diccionario = extraer_fotos(2)
    # print(crear_html(diccionario)) para abrirlo en el navegador se utilizara el with open
    html = crear_html(diccionario)
    show_fotos(html, 'apod')

#esta parte se elimina porque se hizo en el archivo show.py
    #with open('apod.html', 'w') as file:
     #   file.write(html)

    titulos, descripciones, fotos = extraer_planetas(2, 5)
    html = crear_html_planeta(titulos, descripciones, fotos)
    show_fotos(html, 'planetas')

    fotos, horas = extraer_earth()
    html = crear_html_rotacion(fotos, horas)
    show_fotos(html, 'rotacion')