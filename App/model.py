"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
"""

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(type: str) -> dict:
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorias.
    Retorna el catalogo inicializado.
    """
    catalog = {
        'videos': None,
        'categories': None,
        'countries': None,
    }

    catalog['videos'] = lt.newList(type, cmpfunction=None)
    catalog['categories'] = lt.newList(type, cmpfunction=None)
    catalog['countries'] = lt.newList(type, cmpfunction=compare_country)
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog: dict, video: dict) -> None:
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)
    addVideoCountry(catalog, video['country'].strip(), video)


def addCategory(catalog: dict, category: dict) -> None:
    """
    Adiciona una categoria a la lista de categorias
    """
    c = newCategory(category['name'], category['id'])
    lt.addLast(catalog['categories'], c)


def addVideoCountry(catalog: dict, country_name: str, video: dict) -> None:
    """
    Se agregan los videos que pertenecen a cada pais.
    """
    index = lt.isPresent(catalog['countries'], country_name)
    if index > 0:
        country = lt.getElement(catalog['countries'], index)
    else:
        country = newCountry(country_name)
        lt.addLast(catalog['countries'], country)

    lt.addLast(country['videos'], video)


# Funciones para creacion de datos


def newCategory(name: str, id: int) -> dict:
    """
    Esta estructura almancena las categorias utilizados para marcar los videos.
    """
    cat = {'name': '', 'id': ''}
    cat['name'] = name.lstrip()
    cat['id'] = id
    return cat


def newCountry(name: str) -> dict:
    """
    Esta estructura almancena los paises de los videos.
    """
    country = {
        'name': name,
        'videos': lt.newList('ARRAY_LIST'),
    }

    return country


# Funciones de consulta

def findCategory(catalog, category_name):
    for category in lt.iterator(catalog['categories']):
        if category['name'].lower() == category_name.lower():
            return category['id']
    return None


def getVideosByCountry(catalog, country_name):
    """
    Retorna un pais
    """
    index = lt.isPresent(catalog['countries'], country_name)
    if index > 0:
        country = lt.getElement(catalog['countries'], index)
        return country
    return None


def getVideosByCategory(catalog, category_id):
    """
    Retorna videos de una categoria
    """
    dict_category = {}
    dict_category['videos'] = lt.newList('ARRAY_LIST')
    for item in lt.iterator(catalog['videos']):
        if int(item['category_id']) == category_id:
            lt.addLast(dict_category['videos'], item)
    return dict_category

    '''
    index = lt.isPresent(catalog['countries'], category_name)
    if index > 0:
        country = lt.getElement(catalog['countries'], index)
        return country
    return None
    '''

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1: dict, video2: dict) -> bool:
    """
    Devuelve verdadero (True) si los 'views' de video1 son mayores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (int(video1["views"]) > int(video2["views"]))


def compare_country(country_name: str, country: dict) -> bool:
    if country_name.lower() in country['name'].lower():
        return 0
    return -1


# Funciones de ordenamiento


def sortVideos(catalog: dict, algorithm: int) -> tuple:
    sub_list = catalog['videos']
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if int(algorithm) == 1:
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif int(algorithm) == 2:
        sorted_list = sel.sort(sub_list, cmpVideosByViews)
    elif int(algorithm) == 3:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif int(algorithm) == 4:
        sorted_list = quick.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = merge.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list