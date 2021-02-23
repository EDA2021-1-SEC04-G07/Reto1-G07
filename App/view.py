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
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos según su número de vistas son:")
        i=0
        while i <= sample:
            video = lt.getElement(ord_videos,i)
            print("\t Fecha de tendencia:", video['trending_date'])
            print("\t Titulo:", video['title'])
            print("\t Nombre del canal:", video['channel_title'])
            print("\t Fecha de publicación:", video['publish_time'])
            print("\t Vistas:", video['views'])
            print("\t Me gusta:", video['likes'])
            print("\t No me gusta:", video['dislikes'])
            print("\n")
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Seleccione el tipo de lista para cargar la información: ")
        print("1) ARRAY_LIST")
        print("2) SINGLE_LINKED")
        tipo_lista = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            catalog = initCatalog("ARRAY_LIST")
        if int(inputs[0]) == 2:
            catalog = initCatalog("SINGLE_LINKED")
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
        categories = catalog['categories']
        for category in categories['elements']:
            print("\t", category['id'], category['name'])

    elif int(inputs[0]) == 2:
        size = int(input("Indique tamaño de la muestra: "))
        category = input("Seleccione la categoria a buscar: ")
        country = input("Seleccione el pais a bucar: ")
        num = int(input("Buscando los TOP?: "))
        if size <= lt.size(catalog['videos']):
            result = controller.sortVideos(catalog, size)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
            printResults(result[1], num)
        else:
            print("El tamaño de la muestra especificado es mayor al tamaño de la lista.")
            print("Intentelo de nuevo.")

    elif int(inputs[0]) == 3:
        country = input("Seleccione el pais a bucar: ")
        # call to controller

    elif int(inputs[0]) == 4:
        category = input("Seleccione la categoria a buscar: ")
        # call to controller

    elif int(inputs[0]) == 5:
        country = input("Seleccione el pais a bucar: ")
        num = input("Buscando los TOP?: ")
        tag = input("Seleccione la etiqueta a buscar: ")
        # call to controller

    else:
        sys.exit(0)
sys.exit(0)
