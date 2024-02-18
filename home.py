import csv
import os
import json


def leer_csv():
    lista_datos = []
    with open("G:/LPSAPP/LPS_Ferroscan/csvdata/2823_batch_res.csv", 'r') as archivo:
        lector_csv = csv.reader(archivo)
        print (lector_csv)
        for fila in lector_csv:
            #print(', '.join(fila))
            lista_datos.append(fila)
    solo_datos = []

    for fila in lista_datos[3:]:
        solo_datos.append(fila)
        datos_separados = [item.split(';') for item in fila]
        # item = datos_separados(0)
        # print (item)
        # distancia = datos_separados[1]
        # print (distancia)
        # cubierta = datos_separados[2]
        # print (cubierta)
        # diametro = datos_separados[3]
        # print (diametro)
        # overlay = datos_separados[4]    
        # print (overlay)
        # realdiametro = datos_separados[5]
        # print (realdiametro)
        # calidad = datos_separados[6]
        # print (calidad)
        # tipo = datos_separados[7]
        # print (tipo)
        # trazo = datos_separados[8]
        # print (trazo)

    print (datos_separados)
    # Do something with the JSON data
    titulos = solo_datos[0]
    datos_con_titulos = []
    for fila in solo_datos[1:]:
        datos_con_titulos.append(dict(zip(titulos, fila)))
        
        # Do something with the JSON data
    json_data = json.dumps(solo_datos)
        
    with open('data.json', 'w') as file:
        json.dump(solo_datos, file)
    return lista_datos

def obtener_nombres_archivos(directorio = "./csvdata/"):
    nombres_archivos = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".csv"):
            leer_csv(directorio + archivo)

            nombres_archivos.append(archivo)

    return nombres_archivos    

if __name__ == "__main__":
    leer_csv()
