import tkinter as tk
from tkinter import PhotoImage
from ventanaCuentas import VentanaCuentas

class VentanaPanel(tk.Tk):

    def __init__(self):
        super().__init__()

        # Aspectos de la ventana
        """
        self.title("CromaSell")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana principal
        prueba_label = tk.Label(self, text = "Ventana Panel")
        prueba_label.pack()

        agregarCuentas_button = tk.Button(self, text= "Agregar cuenta", command= self.agregar_cuentas)
        agregarCuentas_button.pack()
        """
        self.title("Panel")
        self.geometry("1350x650")  
        self.resizable(width=False, height=False)  
        try:
            self.fondo = PhotoImage(file="code/fondo_m.png")
            self.fondo = self.fondo.subsample(self.fondo.width() // 1350, self.fondo.height() // 650)
            fondo_label = tk.Label(self, image=self.fondo)
            fondo_label.grid(row=0, column=0, rowspan=2, columnspan=1)
        except Exception as e:
            print("Error al cargar la imagen de fondo:", str(e))
            self.fondo = None
#botones
        boton1 = tk.Button(self, text="Inventario", command=self.on_button1_click, width=13, height=4, bg="dark orange", fg="white")
        boton1.place(relx=0.86, rely=0.60, anchor="center")

        boton2 = tk.Button(self, text="Consultar", command=self.on_button2_click, width=13, height=4, bg="dark orange", fg="white")
        boton2.place(relx=0.94, rely=0.60, anchor="center")

        boton3 = tk.Button(self, text="BUSCAR", command=self.on_button3_click, width=13, height=4, bg="dark orange", fg="white")
        boton3.place(relx=0.86, rely=0.71, anchor="center")

        boton4 = tk.Button(self, text="VENTA A CREDITO", command=self.on_button4_click, width=13, height=4, bg="dark orange", fg="white")
        boton4.place(relx=0.94, rely=0.71, anchor="center")

        boton5 = tk.Button(self, text="DESCUENTO", command=self.on_button5_click, width=13, height=4, bg="dark gray", fg="white")
        boton5.place(relx=0.86, rely=0.82, anchor="center")

        boton6 = tk.Button(self, text="VER RECIBO", command=self.on_button6_click, width=13, height=4, bg="dark gray", fg="white")
        boton6.place(relx=0.94, rely=0.82, anchor="center")

        boton7 = tk.Button(self, text="TARJETA", command=self.on_button7_click, width=13, height=2, bg="dark orange", fg="white")
        boton7.place(relx=0.86, rely=0.936, anchor="center")

        boton8 = tk.Button(self, text="EFECTIVO", command=self.on_button8_click, width=13, height=2, bg="dark orange", fg="white")
        boton8.place(relx=0.94, rely=0.936, anchor="center")

    def on_button1_click(self):
        print("Botón 1 clickeado")

    def on_button2_click(self):
        print("Botón 2 clickeado")

    def on_button3_click(self):
        print("Botón 3 clickeado")

    def on_button4_click(self):
        print("Botón 4 clickeado")

    def on_button5_click(self):
        print("Botón 5 clickeado")

    def on_button6_click(self):
        print("Botón 6 clickeado")

    def on_button7_click(self):
        print("Botón 7 clickeado")

    def on_button8_click(self):
        print("Botón 8 clickeado")

    
    def agregar_cuentas(self):
        ventana_cuentas= VentanaCuentas()
        ventana_cuentas.mainloop()

    
if __name__ == '__main__':
    app = VentanaPanel()
    app.mainloop()