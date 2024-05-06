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
    lecturas = 0
    for file in files:
        if file.endswith(".csv"):
            lecturas = lecturas + 1
        else:
            print("No se encontraron archivos CSV")
        getdata = csv.reader(open(file_path + "/" + files[1]))
        for row in getdata:
            datoslist.append(row)
        jsondata = json.dumps(datoslist)
        datos = 3
        for cvslines in datoslist:
            datos = datos + 1
            if datos >= len(datoslist):
                break
        datos = datos - 3
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