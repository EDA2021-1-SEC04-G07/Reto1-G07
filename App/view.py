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
catalog = None


def printMenu() -> None:
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Elegir algortimo de ordenamiento")
    print("3- Encontrar videos trending por pais y categoria")
    print("4- Encontrar video con mas dias de trending por pais")
    print("5- Encontrar video con mas dias de trending por categoria")
    print("6- Ecnontrar videos con mas likes por pais y tag")
    print("7- Salir")


def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, "videos según su número de vistas son:")
        print()
        i = 1
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print("\t Fecha de tendencia:", video['trending_date'])
            print("\t Titulo:", video['title'])
            print("\t Nombre del canal:", video['channel_title'])
            print("\t Fecha de publicación:", video['publish_time'])
            print("\t Vistas:", video['views'])
            print("\t Me gusta:", video['likes'])
            print("\t No me gusta:", video['dislikes'])
            print("\n")
            i += 1


def initCatalog(list_type: str) -> dict:
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(list_type)


def loadData(catalog: dict) -> None:
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def sortVideos(catalog: dict, size: int, algorithm: str):
    """
    Llama a la funcion sortVideos del controlador.
    """
    return controller.sortVideos(catalog, size, alg_type)


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

        if int(list_type[0] == 1):
            list_type = "ARRAY_LIST"
        else:
            list_type = "SINGLE_LINKED"

        catalog = initCatalog(list_type)

        print("Cargando información de los archivos ....")
        loadData(catalog)

        print('Videos cargados:', lt.size(catalog['videos']))
        first_vid = lt.firstElement(catalog['videos'])
        print("Primer video:")
        print("\t Titulo:", first_vid['title'])
        print("\t Nombre del canal:", first_vid['channel_title'])
        print("\t Fecha de tendencia:", first_vid['trending_date'])
        print("\t Pais:", first_vid['country'])
        print("\t Vistas:", first_vid['views'])
        print("\t Me gusta:", first_vid['likes'])
        print("\t No me gusta:", first_vid['dislikes'])

        print('\nCategorias cargadas:')
        for category in lt.iterator(catalog['categories']):
            print("\t" + category['id'] + ": " + category['name'])

        print("\n")

    elif int(inputs[0]) == 2:
        alg_type = int(input("Seleccione el tipo de algoritmo de ordenamiento:"
                             + "\n\t1. Insertion Sort"
                             + "\n\t2. Selection Sort"
                             + "\n\t3. Shell Sort\n"))

        size = int(input("Seleccione el tamaño de la muestra: "))
        # num = int(input("Buscando los TOP?: "))
        if size <= lt.size(catalog['videos']):
            result = sortVideos(catalog, size, alg_type)
            print(
                "Para la muestra de", size, "elementos el tiempo (mseg) es:",
                str(result[0])
            )

            # printResults(result[1], num)
        else:
            print(
                "El tamaño de la muestra especificado es mayor "
                + "al tamaño de la lista."
            )
            print("Intentelo de nuevo.")

    elif int(inputs[0]) == 3:
        num = int(input("Numero de videos a visualizar: "))
        country = input("Pais a buscar: ")
        category = input("Categoria a buscar: ")

    elif int(inputs[0]) == 4:
        country = input("Pais a buscar: ")

    elif int(inputs[0]) == 5:
        category = input("Categoria a buscar: ")

    elif int(inputs[0]) == 6:
        num = int(input("Numero de videos a visualizar: "))
        country = input("Pais a buscar: ")
        tag = input("Tag a buscar: ")

    else:
        sys.exit(0)
sys.exit(0)
