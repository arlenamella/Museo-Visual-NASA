
def show_fotos(html,nombre):
    with open(f'{nombre}.html', 'w') as file:
        file.write(html)

if __name__ == '__main__':
    from apod import extraer_fotos
    from modulo_html import crear_html
    diccionario = extraer_fotos(2)
    html = crear_html(diccionario)
    show_fotos(html, 'apod')