import tkinter as tk
from tkinter import messagebox
from baseDeDatos2 import archivo_JSON
from baseDeDatos2 import BaseDeDatos
import os

class VentanaCuentas(tk.Tk):
    def __init__(self):
        super().__init__()

        # Instancia de BaseDeDatos
        self.mysql = BaseDeDatos()

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

        agregarUsuario_button = tk.Button(self, text= "Agregar cuenta", command= self.agregar_cuenta)
        agregarUsuario_button.pack()

    def agregar_cuenta(self):

        usuario = str(self.usuario_entry.get())
        if self.contrasena_entry.get() != self.contrasena2_entry.get():
            contrasena = self.contrasena2_entry
            messagebox.showerror("Error", "Las contrasenas no coinciden")
            # Establecer conexion a la BD
        else:
            contrasena = str(self.contrasena2_entry)
            try:
                # Conexión a la BD
                datos_JSON = archivo_JSON()
                host, user, password, database = datos_JSON.leer_JSON()
                conn = self.mysql.conexion(host, user, password, database)
                # Evaluar la conexión
                if isinstance(conn, str):
                    messagebox.showerror("No se logro la conexion a la base de datos.\n{conn}")
                    
                else:
                    # Hashear contraseña
                    salt = os.urandom(16)
                    contrasena_hash = self.mysql.hash(contrasena, salt)

                    # Guardar el resultado en la BD
                    save = self.mysql.ejecutar_consulta("INSERT INTO cuentas(usuario, contrasena, salt) VALUES(%s, %s, %s)",(usuario, contrasena_hash, salt))
                    if isinstance(save, str):
                        messagebox.showerror("La cuenta no se creo con exito.", save)
                    else:
                        messagebox.showinfo("Aviso", "Cuenta almacenada con exito")

                    self.mysql.cerrar_conexion()

            except Exception as e:
                    messagebox.showerror("Error de conexíon", str(e))

if __name__ == '__main__':
    app = VentanaCuentas()
    app.mainloop()
