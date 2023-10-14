import tkinter as tk
from ventanaCuentas import VentanaCuentas

class VentanaPanel(tk.Tk):

    def __init__(self):
        super().__init__()

        # Aspectos de la ventana
        self.title("CromaSell")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana principal
        prueba_label = tk.Label(self, text = "Ventana Panel")
        prueba_label.pack()

        agregarCuentas_button = tk.Button(self, text= "Agregar cuenta", command= self.agregar_cuentas)
        agregarCuentas_button.pack()
    
    def agregar_cuentas(self):
        ventana_cuentas= VentanaCuentas()
        ventana_cuentas.mainloop()

    
if __name__ == '__main__':
    app = VentanaPanel()
    app.mainloop()