import tkinter as tk
from tkinter import messagebox
from baseDeDatos import BaseDeDatos
from ventanaPanel import VentanaPanel
from ventanaCuentas import VentanaCuentas
import bcrypt

class VentanaAcceso(tk.Tk,):

    def __init__(self):
        super().__init__()

        # Instancia BaseDeDatos
        self.mysql = BaseDeDatos()

    
    def atributosVentana(self):
    
        # Atributos de la ventana
        self.title("Acceso")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.iconbitmap("img/logo t.ico")

        usuario_label = tk.Label(self, text= "Usuario:")
        usuario_label.pack()
        self.usuario_entry = tk.Entry(self) # Se deja como atributo general "self.", pq despues se recolecta lo que almacena
        self.usuario_entry.pack()

        #Frame para la contrasena
        contrasena_label = tk.Label(self, text= "Contraseña")
        contrasena_label.pack()
        self.contrasena_entry = tk.Entry(self)
        self.contrasena_entry.pack()

        acceso_button = tk.Button(self, text = "Iniciar Sesión", command = self.acceso)
        acceso_button.pack()

        # Boton para crear una cuenta para accesar
        crearCuenta_button = tk.Button(self, text = "Crear cuenta", command = self.crear_cuenta)
        crearCuenta_button.pack()

    
    def acceso(self):
        try:
            # Credenciales ingresadas
            usuario = self.usuario_entry.get()
            contrasena_in = self.contrasena_entry.get()
            contrasena = str(contrasena_in)

            # Base de datos
            conexion = self.mysql.conexion()
            if conexion is True:
                bool_consulta, consulta = self.mysql.obtener_datos("SELECT contrasena, salt FROM cuentas WHERE usuario = %s", (usuario, ))
                if bool_consulta is True:
                    try:
                        # Credenciales obtenidas de la base de datos
                        for fila in consulta:
                            contrasena_bd = fila[0]
                            salt_bd = fila[1]
                        # Evaluar las credenciales ingresadas con las obtenidas de la bd
                            # aplicar hash a la contrasena
                        #messagebox.showwarning("probar cadena contrasena", contrasena)
                        salt_bytes = salt_bd.encode("utf-8")
                        contrasena_hash = bcrypt.hashpw(contrasena.encode("utf-8"), salt_bytes)
                        if contrasena_hash == contrasena_bd.encode("utf-8"):
                            ventanapanel = VentanaPanel()
                            ventanapanel.mainloop()
                        else:
                            messagebox.showwarning(None, f"La contrasena es incorrecta:\npass_bd: {contrasena_bd}\npass_in: {contrasena_hash}")
                    except Exception as e:
                        messagebox.showwarning(None, e)
                else:
                    messagebox.showerror("Error en la consulta", consulta)
            else:
                messagebox.showerror("Error en la conexion", conexion)

        except Exception as e:
            messagebox.showwarning(None, e)

    def crear_cuenta(self):
        ventanaCuentas = VentanaCuentas()
        ventanaCuentas.mainloop()
        

if __name__ == '__main__':

    app = VentanaAcceso()
    app.atributosVentana()
    app.mainloop()