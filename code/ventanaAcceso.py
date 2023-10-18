import tkinter as tk
from tkinter import messagebox
from baseDeDatos2 import BaseDeDatos
from baseDeDatos2 import archivo_JSON
from ventanaPanel import VentanaPanel

class VentanaAcceso(tk.Tk):

    def __init__(self):
        super().__init__()

        # Instancia BaseDeDatos
        self.mysql = BaseDeDatos()

        # Atributos de la ventana
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
        contrasena = self.mysql.hash(self.contrasena_entry.get())

        # Importar las credenciales de acceso a la BD
        datos_JSON = archivo_JSON()
        host, user, password, database = datos_JSON.leer_JSON()
        # Conexión a la BD
        conn = self.mysql.conexion(host, user, password, database)
        if isinstance(conn, str):
            messagebox.showerror("Error", conn)
        else:
            messagebox.showinfo("Aviso", "Conexión exitosa")
            #self.mysql.cerrar_conexion()
            credenciales_bd = self.mysql.obtener_datos("SELECT COUNT(*) FROM cuentas WHERE usuario = %s and contrasena = %s", (usuario, contrasena))

            if isinstance(credenciales_bd, str):
                messagebox.showerror("Error", credenciales_bd)
            else:
                """
                resultado = credenciales_bd[0]
                if resultado > 0:
                    ventanaPanel = VentanaPanel()
                    ventanaPanel.mainloop()
                else:
                    messagebox.showwarning("Aviso", "Cuenta no encontrada")
                """
                messagebox.showinfo("aviso", credenciales_bd)

if __name__ == '__main__':

    app = VentanaAcceso()
    app.mainloop()