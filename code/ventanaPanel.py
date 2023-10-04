import tkinter as tk

class VentanaPanel(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Panel")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        prueba_label = tk.Label(self, text = "Ventana Panel")
        prueba_label.pack()
    
if __name__ == '__main__':
    app = VentanaPanel()
    app.mainloop()