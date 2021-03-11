"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoria y pais")
    print("3- Encontrar video tendencia por pais")
    print("4- Encontrar video tendencia por categoria")
    print("5- Buscar los videos con mas Likes")
    print("0- Salir")


def initCatalog(type:str):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(type)


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def printResults(ord_videos, sample=10):
    """Imprime los 'sample' videos para el requerimiento 1"""
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos según su número de vistas son:\n")
        i = 1
        while i <= sample:
            video = lt.getElement(ord_videos,i)
            print("\t Fecha de tendencia:", video['trending_date'])
            print("\t Titulo:", video['title'])
            print("\t Nombre del canal:", video['channel_title'])
            print("\t Fecha de publicación:", video['publish_time'])
            print("\t Vistas:", video['views'])
            print("\t Me gusta:", video['likes'])
            print("\t No me gusta:", video['dislikes'])
            print()
            i += 1


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        list_type = input("Seleccione el tipo de lista:"
                          + "\n\t1. ARRAY_LIST"
                          + "\n\t2. SINGLE_LINKED\n")

        if int(list_type[0]) == 1:
            list_type = "ARRAY_LIST"
        else:
            list_type = "SINGLE_LINKED"

        catalog = initCatalog(list_type)
        print("Cargando información de los archivos ....")
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print("Primer video:")
        first_vid = lt.firstElement(catalog['videos'])
        print("\t Titulo:", first_vid['title'])
        print("\t Nombre del canal:", first_vid['channel_title'])
        print("\t Fecha de tendencia:", first_vid['trending_date'])
        print("\t Pais:", first_vid['country'])
        print("\t Vistas:", first_vid['views'])
        print("\t Me gusta:", first_vid['likes'])
        print("\t No me gusta:", first_vid['dislikes'])
        print('Categorias cargadas:')
        i = 1
        while i <= lt.size(catalog['categories']):
            category = lt.getElement(catalog["categories"],i)
            print("\t", category['id'], category['name'])
            i += 1

    elif int(inputs[0]) == 2:
        category_name = input("Seleccione la categoria a buscar: ")
        country_name = input("Seleccione el pais a bucar: ")
        num = int(input("Buscando los TOP?: "))
        country = controller.getVideosByCountry(catalog, country_name)
        category = controller.findCategory(catalog, category_name)
        country_cat = controller.getVideosByCategory(country, int(category))
        result = controller.sortVideos(country_cat)
        printResults(result[1], num)

    elif int(inputs[0]) == 3:
        country_name = input("Seleccione el pais a bucar: ")
        country = controller.getVideosByCountry(catalog, country_name)
        country = controller.sortVideos(country)
        video = controller.getTrendingVideo(country[1])
        print()
        print("\t Titulo:", video[0]['title'])
        print("\t Nombre del canal:", video[0]['channel_title'])
        print("\t Pais:", video[0]['country'])
        print("\t Numero de dias:", video[1])
        print()

    elif int(inputs[0]) == 4:
        category_name = input("Seleccione la categoria a buscar: ")
        category_id = controller.findCategory(catalog, category_name)
        category = controller.getVideosByCategory(catalog, int(category_id))
        trend = controller.calcTrendingDays(category)
        result = controller.sortVideosByTrend(trend)
        first_vid = lt.firstElement(result[1])
        print("El video que más días estuvo en trending para la categoría " + '"' + category_name + '" fue:')
        print("\t Titulo:", first_vid['title'])
        print("\t Nombre del canal:", first_vid['channel_title'])
        print("\t ID de categoria:", first_vid['category_id'])
        print("\t Días en trending:", first_vid['trending_total'])

    elif int(inputs[0]) == 5:
        country_name = input("Seleccione el pais a bucar: ")
        num = int(input("Buscando los TOP?: "))
        tag = input("Seleccione la etiqueta a buscar: ")
        country = controller.getVideosByCountry(catalog, country_name)
        videos_tag = controller.findTag(country, tag)
        result = controller.sortVideosByLikes(videos_tag)
        i = 1
        print("Los {n} videos con más likes con el tag '{tag}' fueron:".format(n=num, tag=tag))
        while i <= num:
            first_vid = lt.getElement(result[1], i)
            print("\t Titulo:", first_vid['title'])
            print("\t Nombre del canal:", first_vid['channel_title'])
            print("\t Fecha de publicación:", first_vid['publish_time'])
            print("\t Vistas:", first_vid['views'])
            print("\t Me gusta:", first_vid['likes'])
            print("\t No me gusta:", first_vid['dislikes'])
            print("\t Etiquetas:")
            tags = first_vid['tags'].replace('"', '')
            tag_list = tags.split('|')
            for tag in tag_list:
                print("\t\t", tag)
            i += 1
    else:
        sys.exit(0)
sys.exit(0)
