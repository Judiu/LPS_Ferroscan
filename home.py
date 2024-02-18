import csv
import os


def leer_csv():
    lista_datos = []
    with open("G:/LPSAPP/LPS_Ferroscan/csvdata/2823_batch_res.csv", 'r') as archivo:
        lector_csv = csv.reader(archivo)
        print (lector_csv)
        for fila in lector_csv:
            #print(', '.join(fila))
            lista_datos.append(fila)
    datos_fila = lista_datos[3]
    print (datos_fila)
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
