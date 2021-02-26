import config as cf
import sys
import controller
import csv
from DISClib.ADT import list as lt
assert cf
print("Cargando datos para testear...")
testfile = cf.file_dir + '/App/test.csv'
resultados_file = cf.file_dir + '/App/resultados.csv'
input_file = csv.DictReader(open(testfile, encoding='utf-8'),delimiter=',')
i = 0
for line in input_file:
    i += 1
print(i,"Tests cargados correctamente")
print("Cargando videos en un array...")
array = controller.initCatalog('ARRAY_LIST')
controller.loadData(array)
print(lt.size(array['videos']),"videos cargados correctamente...")
print("Cargando videos en una lista encadenada...")
linked = controller.initCatalog('SINGLE_LINKED')
controller.loadData(linked)
print(lt.size(linked['videos']),"videos cargados correctamente...")

input_file = csv.DictReader(open(testfile, encoding='utf-8'),delimiter=',')

header = "lista,algoritmo,datos,resultado"
output_file = open(resultados_file, 'w')
output_file.write(header)
output_file.write('\n')
output_file.close()
j = 0
print(j,'de', i, 'test completados', round((j/i)*100),'%')
for test in input_file:
    output_file = open(resultados_file, 'a')
    print('test:',j+1)
    lista = test['lista']
    size = int(test['datos'])
    algoritmo = int(test['algoritmo'])
    print('\tTipo de lista:',lista)
    print('\tAlgoritmo:',algoritmo)
    print('\tDatos:',size)
    if lista == 'array':
        result = controller.sortVideos(array, size, algoritmo)
    elif lista == 'linked':
        result = controller.sortVideos(linked, size, algoritmo)
    intento = ",".join([str(lista), str(algoritmo), str(size), str(result[0])])
    print('Tiempo:',result[0],'ms.')
    print("Guardando datos...")
    output_file.write(intento)
    output_file.write('\n')
    output_file.close()
    print("Datos guardados...\n")

    j += 1
    print(j,'de', i, 'test completados', round((j/i)*100),'%')


print("Finalizado.")

