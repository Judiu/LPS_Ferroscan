import tkinter as tk

def calcular_trazo():
    # Obtener los valores ingresados por el usuario
    variable = variable_entry.get()
    trazo = trazo_entry.get()

    # Realizar el cálculo del trazo aquí
    # ...

    # Mostrar el resultado en una ventana emergente
    resultado = tk.Toplevel(root)
    resultado.title("Resultado")
    resultado.geometry("200x100")
    resultado_label = tk.Label(resultado, text="El trazo calculado es: ")
    resultado_label.pack()
    resultado_valor = tk.Label(resultado, text="Resultado aquí")
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

calcular_button = tk.Button(root, text="Calcular", command=calcular_trazo)
calcular_button.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()
