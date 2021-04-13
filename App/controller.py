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
 """

import config as cf
import model
import csv
import time
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos


def initCatalog(list_type: str) -> dict:
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(list_type)
    return catalog

# Funciones para la carga de datos


def loadData(catalog: dict) -> tuple:
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """


    # TODO: modificaciones para medir el tiempo y memoria
    # respuesta por defecto
    delta_time = -1.0
    delta_memory = -1.0

    # inicializa el processo para medir memoria
    tracemalloc.start()

    # toma de tiempo y memoria al inicio del proceso
    start_time = getTime()
    start_memory = getMemory()

    loadCategories(catalog)
    loadVideos(catalog)

    # toma de tiempo y memoria al final del proceso
    stop_memory = getMemory()
    stop_time = getTime()

    # finaliza el procesos para medir memoria
    tracemalloc.stop()

    # calculando la diferencia de tiempo y memoria
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory


def loadVideos(catalog: dict) -> None:
    """
    Carga los videos del archivo.
    """
    directory = cf.data_dir + "videos/videos-large.csv"
    file = csv.DictReader(open(directory, encoding="utf-8"))
    for video in file:
        model.addVideo(catalog, video)


def loadCategories(catalog: dict) -> None:
    """
    Carga las categorias del archivo.
    """
    directory = cf.data_dir + "videos/category-id.csv"
    file = csv.DictReader(open(directory, encoding="utf-8"), delimiter='\t')
    for category in file:
        model.addCategory(catalog, category)


# Funciones de ordenamiento


def sortVideos(catalog: dict, algorithm: int = 5):
    """
    Ordena los videos por views.
    """
    return model.sortVideos(catalog, algorithm)
    
def sortVideosByLikes(catalog: dict):
    """
    Ordena los videos por likes.
    """
    return model.sortVideosByLikes(catalog)

def sortVideosByTrend(catalog: dict):
    """
    Ordena los videos por dias en trending.
    """
    return model.sortVideosByTrend(catalog)

# Funciones de consulta sobre el catálogo

def getVideosByCountry(catalog, country_name):
    """
    Retorna los videos por pais
    """
    country = model.getVideosByCountry(catalog, country_name)
    return country


def findCategory(catalog, category_name):
    """Encuentra el id de la categoría según el nombre y lo retorna."""
    return model.findCategory(catalog, category_name)


def getVideosByCategory(catalog, category_id):
    """
    Retorna los videos por categoria a partir de su id
    """
    cat = model.getVideosByCategory(catalog, category_id)
    return cat

def calcTrendingDays(catalog):
    """Calcula los días que estuvieron en trending los videos y retorna una nueva TAD lista con este nuevo dato ('trending_total')."""
    return model.calcTrendingDays(catalog)

def getTrendingVideo(catalog: dict) -> tuple:
    return model.getTrendingVideo(catalog)

def findTag(catalog, tag_name):
    return model.findTag(catalog, tag_name)

# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory