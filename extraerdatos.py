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
    for file in files:
        print(file)
    verificardatos(files, file_path)

def verificardatos(files, file_path):
    lecturas = 0
    for file in files:
        if file.endswith(".csv"):
            print("Archivo CSV encontrado: " + file)
            lecturas = lecturas + 1
        else:
            print("No se encontraron archivos CSV")
    print("Numero de archivos CSV encontrados: " + str(lecturas))
    print(files)


if __name__ == '__main__':
    obtenerdatos()