import tkinter as tk
from tkinter import messagebox
from baseDeDatos import BaseDeDatos
from ventanaPanel import VentanaPanel

class VentanaAcceso(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Acceso")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana "Acceso"

        usuario_label = tk.Label(self, text = "Usuario")
        usuario_label.pack(pady = 10)

        self.usuario_entry = tk.Entry(self) # Se deja como atributo general "self.", pq despues se recolecta lo que almacena
        self.usuario_entry.pack(pady = 5)

        contrasena_label = tk.Label(self, text = "Contrasena")
        contrasena_label.pack()

        self.contrasena_entry = tk.Entry(self, show = "*")
        self.contrasena_entry.pack(pady = 5)

        acceso_button = tk.Button(self, text = "Iniciar Sesión", command = self.acceso)
        acceso_button.pack(pady = 10)
    
    def acceso(self):
        # Obtener datos tanto de "Usuario", como de "Contrasena"
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        # Instancia de la clase "BaseDeDatos"
        bd = BaseDeDatos()
        # Consulta a la BD
        bd.cursor.execute("SELECT contrasena FROM usuarios WHERE usuario= ?", (usuario,))
        resultado = bd.cursor.fetchone()
        # Validacion de credenciales
        if resultado:
            contrasena_guardada = resultado[0]
            if contrasena == contrasena_guardada:

                self.destroy()
                ventana_principal = VentanaPanel()
                ventana_principal.mainloop()
                bd.cerrar_conexion()
            else:
                messagebox.showerror("Aviso", "La contraseña es incorrecta.")
        else:
            messagebox.showerror("Aviso", "Nombre de usuario no encontrado.")

if __name__ == '__main__':

    app = VentanaAcceso()
    app.mainloop()