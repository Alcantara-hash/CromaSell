import tkinter as tk
from baseDeDatos2 import BaseDeDatos

class VentanaCuentas(tk.Tk):
    def __init__(self):
        super().__init__()

        # Instancia de BaseDeDatos
        self.bd = BaseDeDatos

        # Aspectos de la ventana
        self.title("CromaSell")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana principal
        prueba_label = tk.Label(self, text = "Ventana Panel")
        prueba_label.pack()

        agregarCuentas_button = tk.Button(self, text= "Agregar cuenta", command= self.agregar_cuentas)
        agregarCuentas_button.pack()