# Museo-Visual-NASA

### ejemplo de conexión y consumo de APIs



Combina los conocimientos de los módulos previos con información extraída mediante API para agregar versatilidad y robustez a sus aplicaciones.

## Descripción

El museo de la NASA se caracteriza por almacenar grandes hitos de la historia de la humanidad en cuanto a la carrera espacial. La información que maneja la NASA es enorme, tanto así, que podrían pasar años tratando de explorarse a cabalidad.
Existe una parte de esta información que es gráfica, y la NASA está pensando en disponibilizarla a la comunidad de una manera amigable. El objetivo de la NASA en particular es permitir a cualquier persona acceder a fotos emblemáticas tomadas por ellos.
Para ello se te solicita poder prototipar una APP sencilla, ya que actualmente esta información se disponibiliza solo mediante la API de la NASA.
Por lo tanto, se solicita considerar los siguientes tres aspectos:
● La Imagen del día: Varias Imágenes que tienen un significado especial para la NASA y el mundo. ● Fotos de Planetas: Distintas fotos emblemáticas relacionadas con nuestro Sistema Solar. ● Fotos de la Rotación de la Tierra: Para cada día de la historia, los satélites que orbitan alrededor del planeta toman una foto por hora de nuestro planeta.
En este caso se confía en lo que has aprendido a lo largo del módulo, por lo que sólo se entregarán requerimientos generales de lo que se espera. Tendrás la libertad de implementarlo como estime conveniente.
¿Qué tenemos que saber para enfrentarnos a esta prueba?
● Necesitarás de una API Key para poder hacerle consultas a la API de la Nasa. Puede seguir el paso a paso explicado en la lectura en los capítulos API con autenticación e ingresar al Portal de la Nasa para autenticarse.

## Requerimientos

1.	Imagen del Día: La NASA ha disponibilizado una API llamada la Imagen del día (APOD en inglés). Esta API almacena distinta información acerca de esta foto emblemática. Para extraerla se presenta la siguiente documentación:
● Se solicita generar una feature que permita descargar un número definido de Imágenes del día. Este número vendrá dado por el usuario.
○ Atención, asegúrate de que la información que se extraiga sea realmente una imagen. A veces hay videos, y para evitar el manejo de gran cantidad de datos es preferible dejarlos fuera.
● Se solicita que para cada foto del día se muestre: ○ Su nombre o título asociado ○ Fecha ○ Descripción
2.	Planetas: La NASA cuenta también con una biblioteca abierta de imágenes. En esta biblioteca es posible buscar cualquier elemento disponible. Por lo tanto la utilizaremos para extraer información correspondiente a planetas.
Se cuenta con la siguiente documentación: La URL es: https://images-api.nasa.gov
La documentación de esta API es un poco escueta, pero de acuerdo a la información entregada será necesario realizar una consulta en dos etapas:
● Se utilizará una búsqueda, en este caso del nombre del planeta (en inglés) y desde acá se rescatará la siguiente información: ○ nasa_id ○ Título de la Foto ○ Descripción
● Teniendo el nasa_id es posible acceder a los assets para extraer varias versiones de la foto.
● Para esta feature se pide que el usuario escoja un planeta, y el número de fotos que desea obtener de manera aleatoria.
3.	Rotación de la Tierra: En este caso la NASA ha disponibilizado su cámara policromática para poder tomar fotografías de la Tierra mientras rota. Para ello se disponibiliza la siguiente documentación:
● En este caso también se pide observar la documentación para extraer imágenes y fecha/hora en la que se obtuvo la foto.
● La extracción de esta parte también será en dos etapas. Buscando el nombre de las imágenes dada una fecha ingresada por el usuario.
● Con el nombre es posible extraer las imágenes y alinearlas con su respectiva fecha/hora.
● En este caso se deben extraer todas las fotos para la fecha dada.
○ Al parecer se puede extraer como fecha máxima datos del día anterior.
4.	Todas estas features deben estar disponibles mediante un menú interactivo que permita al usuario ingresar todas las opciones necesarias para el uso de cada una.
Además se debe buscar un mecanismo para visualizar toda esta información (no será posible en el terminal). Una sugerencia es poder visualizar todo en un formato HTML, pero la decisión final queda a criterio suyo.











