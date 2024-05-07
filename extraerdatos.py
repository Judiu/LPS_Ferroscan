import csv
import os
import json
import tkinter as tk
from tkinter import filedialog

# Selecionar folder donden se encuentran los Datos del Ferroscan
def obtenerdatos():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    print(file_path)
    # Mostrar archivos en file_path
    files = os.listdir(file_path)
    verificardatos(files, file_path)
    return file_path

def verificardatos(files, file_path):
    datoslist = []
    lecturas_ferro = []

    #Obtener nombre de lectura del Ferroscan SU CODIGO de 4 digitos
    for namefile in files:
        nombre_lectura = namefile[4:8]
        lecturas_ferro.append(nombre_lectura)

    lecturas = 0
    archivo_leido = 0
    solo_datos = []
    for file in files:
        if file.endswith(".csv"):
            lecturas = lecturas + 1
        else:
            print("No se encontraron archivos CSV")
        with open(file_path + "/" + files[archivo_leido], 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                datoslist.append(fila)
                for fila in datoslist[3:]:
                    datoslist = [item.split(';') for item in fila]
                    lista_separada = [element for sublist in datoslist for item in sublist for element in item.split(',')]
                    item = lista_separada[0].replace(" ", "")
                    distancia = lista_separada[1].replace(" ", "")
                    cubierta = lista_separada[2].replace(" ", "")
                    diametro = lista_separada[3].replace(" ", "")
                    overlay = lista_separada[4].replace(" ", "")
                    realdiametro = lista_separada[5].replace(" ", "")
                    calidad = lista_separada[6].replace(" ", "")
                    tipo = lista_separada[7].replace(" ", "")
                    trazo = lista_separada[8].replace(" ", "")
                    solo_datos.append({'item': item, 'distancia': distancia, 'cubierta': cubierta, 'diametro': diametro, 'overlay': overlay, 'realdiametro': realdiametro, 'calidad': calidad, 'tipo':      tipo, 'trazo': trazo})
                
        

        archivo_leido = archivo_leido + 1
        if archivo_leido >= len(files):
            break  
    print(solo_datos)
        # print ("Para el archivo " + files[1] + " se encontraron " + str(datos) + " datos")
        # obtener_promedio_diametro(datoslist)
        # print("El promedio de diametro es: " + str(obtener_promedio_diametro(datoslist)))
    
def obtener_promedio_diametro(datoslist):
    datos = 3
    promedio = []
    for cvslines in datoslist:
        line_data = datoslist[datos]
        line_data = line_data[0].split(";")
        line_data_espacios = line_data[3]
        line_data_espacios = line_data_espacios[5:]
        line_data_espacios = line_data_espacios.replace("mm","")
        line_data_espacios = int(line_data_espacios)
        promedio.append(line_data_espacios)
        datos = datos + 1
        if datos >= len(datoslist):
            break
    promedio_diametro = sum(promedio)/len(promedio)
    return promedio_diametro

if __name__ == '__main__':
    obtenerdatos()