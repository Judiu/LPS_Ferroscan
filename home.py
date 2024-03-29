import csv
import os
import json


def leer_csv(variable = 2823, segmento = 5):
    lista_datos = []
    path = "G:/LPSAPP/LPS_Ferroscan/csvdata/" + str(variable) + "_batch_res.csv"
    with open(path, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        print (lector_csv)
        for fila in lector_csv:
            #print(', '.join(fila))
            lista_datos.append(fila)
    solo_datos = []

    for fila in lista_datos[3:]:
        datos_separados = [item.split(';') for item in fila]
        lista_separada = [element for sublist in datos_separados for item in sublist for element in item.split(',')]
        item = lista_separada[0].replace(" ", "")
        distancia = lista_separada[1].replace(" ", "")
        cubierta = lista_separada[2].replace(" ", "")
        diametro = lista_separada[3].replace(" ", "")
        overlay = lista_separada[4].replace(" ", "")
        realdiametro = lista_separada[5].replace(" ", "")
        calidad = lista_separada[6].replace(" ", "")
        tipo = lista_separada[7].replace(" ", "")
        trazo = lista_separada[8].replace(" ", "")
        solo_datos.append({'item': item, 'distancia': distancia, 'cubierta': cubierta, 'diametro': diametro, 'overlay': overlay, 'realdiametro': realdiametro, 'calidad': calidad, 'tipo': tipo, 'trazo': trazo})
    # Do something with the JSON data        
    json_data = json.dumps(solo_datos)
    if os.path.exists('./data.json'):
        print("El archivo existe")
    else:
        with open('data.json', 'w') as file:
            json.dump(solo_datos, file)
    i = 0
    promedio_diametro = 0
    maximo_diametro = 0
    numero_segmentos = 0
    for items in solo_datos:
        if solo_datos[i]["trazo"] == str(segmento):
            solo_datos[i]["diametro"] = solo_datos[i]["diametro"].replace(" ", "").replace("mm", "")
            promedio_diametro = promedio_diametro + float(solo_datos[i]["diametro"])
            maximo_diametro = maximo_diametro + 1
            numero_segmentos = numero_segmentos + 1
        else:
            asd = 0
        i = i + 1
    print("El numero de segmentos es: " + str(numero_segmentos))
    print(promedio_diametro/maximo_diametro)
    resultado = promedio_diametro/maximo_diametro
    return str(resultado)

def obtener_nombres_archivos(directorio = "./csvdata/"):
    nombres_archivos = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".csv"):
            leer_csv(directorio + archivo)
            nombres_archivos.append(archivo)

    return nombres_archivos    

if __name__ == "__main__":
    leer_csv()
