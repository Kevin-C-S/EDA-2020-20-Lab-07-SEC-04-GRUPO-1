"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

"""
if isEmpty(lst):
6                    return lst
7                 else:
8                     elem = removeLast(lst)
9                     reverse(lst)
10                   addFirst(lst, elem)
11                   return lst
"""

def newTree():
    ver=True
    seguir=True
    contador=0
    cont = {'OCCURRED_ON_DATE': None, #Va
               'INCIDENT_NUMBER': None, #Va
               # Necesario Severity, por eso Incident Number
               'Lat': None, #Va
               'Long': None, #Va
               'Location': None} #Va
    
    # 'key': key, 'value': value, 'size': size, 'left': None, 'right': None, 'type': 'BST'
    newMap()
    while ver == True:
        if seguir:
            cont['OCCURRED_ON_DATE']=lt.newList("ARRAY_LIST",cmpfunction=compare_str)
            key=cont['OCCURRED_ON_DATE']
            cont['INCIDENT_NUMBER']=lt.newList("ARRAY_LIST",cmpfunction=compare_num)
            cont['Lat']=lt.newList("ARRAY_LIST",cmpfunction=compare_num)
            cont['Long']=lt.newList("ARRAY_LIST",cmpfunction=compare_num)
            cont['Location']=lt.newList("ARRAY_LIST",cmpfunction=compare_str)
            value= (cont['INCIDENT_NUMBER'], cont['Lat'], cont['Long'], cont['Location'])
            contador+=1
            if contador<len('OCCURRED_ON_DATE'):
                seguir=False
        else:
            ver=False
        put("RBT", key, value)

def put(map, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        map: La tabla de simbolos ordenada
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
    Returns:
        La tabla de simbolos
    Raises:
        Exception
    """
    return om.put(map, key, value)

def newMap(omaptype='RBT', comparefunction=None):
    """
    Crea una tabla de simbolos ordenada.
    Args:
        maptype: El tipo de map ordenado a utilizar
                 'BST' o 'RBT'
    Returns:
       La tabla de símbolos ordenada sin elementos
    Raises:
        Exception
    """
    return om.newMap(omaptype, comparefunction)

    #PROCESOS
# Funciones para agregar informacion al catalogo


# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones de Comparacion
# ==============================

def compare_str(keyname, value):

    compare = me.getKey(value)
    if (keyname == compare):
        return 0
    elif (keyname > compare):
        return 1
    else:
        return -1

def compare_num(keyname, value):

    compare = float(me.getKey(value))
    if (float(keyname) == compare):
        return 0
    elif (float(keyname) > compare):
        return 1
    else:
        return -1
