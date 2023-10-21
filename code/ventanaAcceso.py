import tkinter as tk
from tkinter import messagebox
from baseDeDatos2 import BaseDeDatos
from baseDeDatos2 import archivo_JSON
from ventanaPanel import VentanaPanel
from ventanaCuentas import VentanaCuentas

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

        siguiente_button = tk.Button(self, text = "Siguiente", command= self.pedir_contrasena)

        contrasena_label = tk.Label(self, text = "Contrasena")
        contrasena_label.pack()
        
        self.contrasena_entry = tk.Entry(self, show = "*")
        self.contrasena_entry.pack(pady = 5)

        acceso_button = tk.Button(self, text = "Iniciar Sesión", command = self.acceso)
        acceso_button.pack(pady = 10)

        crearCuenta_button = tk.Button(self, text = "Crear cuenta", command = self.crear_cuenta)
        crearCuenta_button.pack()
    
    def acceso(self):
        
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        # Conexión a la BD
        datos_JSON = archivo_JSON()
        host, user, password, database = datos_JSON.leer_JSON()
        conn = self.mysql.conexion(host, user, password, database)
        # Evaluar la conexión
        if isinstance(conn, str):
            messagebox.showerror("Error", conn)

        else:
            messagebox.showinfo("Aviso", "Conexión exitosa")

            contrasena_hash = self.mysql.hash()

            credenciales_bd = self.mysql.obtener_datos("SELECT * FROM cuentas WHERE usuario = %s and contrasena = %s", (usuario, contrasena))
            if isinstance(credenciales_bd, str):
                messagebox.showerror("Error", credenciales_bd)
            else:
                for dato in credenciales_bd:
                    print(dato)

            for dato in credenciales_bd:
                print(dato)
                #messagebox.showinfo("aviso", credenciales_bd)
    
    def pedir_contrasena(self):
        pass

    def crear_cuenta(self):
        #self.withdraw()
        ventanaCuentas = VentanaCuentas()
        ventanaCuentas.mainloop()
        

if __name__ == '__main__':

    app = VentanaAcceso()
    app.mainloop()