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


def loadData(catalog: dict) -> None:
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)


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