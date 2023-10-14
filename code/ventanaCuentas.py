import tkinter as tk
from tkinter import messagebox
from baseDeDatos2 import BaseDeDatos

class VentanaCuentas(tk.Tk):
    def __init__(self):
        super().__init__()

        # Aspectos de la ventana
        self.title("Administrar cuentas")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana principal
        usuario_label = tk.Label(self, text= "Usuario:")
        usuario_label.pack(pady = 10)

        self.usuario_entry = tk.Entry(self) # Se deja como atributo general "self.", pq despues se recolecta lo que almacena
        self.usuario_entry.pack(pady = 5)

        contrasena_label = tk.Label(self, text= "Contrasena:")
        contrasena_label.pack()

        self.contrasena_entry = tk.Entry(self, show = "*")
        self.contrasena_entry.pack(pady = 5)

        contrasena2_label = tk.Label(self, text= "Confirma tu contrasena:")
        contrasena2_label.pack()

        self.contrasena2_entry = tk.Entry(self, show= "*")
        self.contrasena2_entry.pack(pady = 5)

        agregarUsuario_button = tk.Button(self, text= "Agregar cuenta", command= self.agregar_cuentas)
        agregarUsuario_button.pack()

    def agregar_cuentas(self):

        usuario = self.usuario_entry.get()
        if self.contrasena_entry.get() == self.contrasena2_entry.get():
            contrasena = self.contrasena2_entry.get()
        else:
            messagebox.showwarning("Aviso", "Las contraseñas no coinciden.")
        
        # Instancia de BaseDeDatos
        """
        try:
            self.db = BaseDeDatos("127.0.0.1", "root", "", "")

        except mysql.connector.Error as error:
            messagebox.showerror("")
        """

if __name__ == '__main__':
    app = VentanaCuentas()
    app.mainloop()
