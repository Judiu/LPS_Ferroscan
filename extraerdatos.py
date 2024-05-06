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

def askuservalues ():
    root = tk.Tk()
    root.withdraw()
    

    

def verificardatos(files, file_path):
    datoslist = []
    lecturas = 0
    for file in files:
        if file.endswith(".csv"):
            lecturas = lecturas + 1
        else:
            print("No se encontraron archivos CSV")
    getdata = csv.reader(open(file_path + "/" + files[0]))
    for row in getdata:
        datoslist.append(row)
    jsondata = json.dumps(datoslist)
    datos = 3
    for cvslines in datoslist:
        print(datoslist[datos])
        datos = datos + 1

    # if os.path.exists('./jsondata.json'):
    #     print("El archivo existe")
    # else:
    #     with open('jsondata.json', 'w') as file:
    #         json.dump(datoslist, file)

if __name__ == '__main__':
    askuservalues()