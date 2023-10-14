import tkinter as tk
from baseDeDatos2 import BaseDeDatos

class VentanaPanel(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("CromaSell")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana principal

        prueba_label = tk.Label(self, text = "Ventana Panel")
        prueba_label.pack()

        agregarCuentas_button = tk.Button(self, text= "Agregar cuenta", command= self.agregar_cuentas)
        agregarCuentas_button.pack()
    
    def agregar_cuentas(self):
        pass

    
if __name__ == '__main__':
    app = VentanaPanel()
    app.mainloop()