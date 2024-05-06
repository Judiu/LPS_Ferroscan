import tkinter as tk
import home
import extraerdatos
from tkinter import filedialog

def obtenerdatos():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    print(file_path)

def calcular_trazo():
    # Obtener los valores ingresados por el usuario
    variable = variable_entry.get()
    trazo = trazo_entry.get()
    filepath = filepath_entry.get()
    # Realizar el cálculo del trazo aquí
    promedio_diamtro = home.leer_csv(variable, trazo)

    # Mostrar el resultado en una ventana emergente
    resultado = tk.Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry("200x100")
    resultado_label = tk.Label(resultado, text="El trazo calculado es: ")
    resultado_label.pack()
    resultado_valor = tk.Label(resultado, text=str(promedio_diamtro))
    resultado_valor.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Trazo")
root.geometry("1080x720")

# Crear los elementos de la interfaz
variable_label = tk.Label(root, text="Variable de cuatro números:")
variable_label.pack()
variable_entry = tk.Entry(root)
variable_entry.pack()

trazo_label = tk.Label(root, text="Trazo a calcular:")
trazo_label.pack()
trazo_entry = tk.Entry(root)
trazo_entry.pack()

filepath_label = tk.Button(root, text="Ruta del archivo:", command=obtenerdatos)
filepath_label.pack()

calcular_button = tk.Button(root, text="Calcular", command=calcular_trazo)
calcular_button.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()
