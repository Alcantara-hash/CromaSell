import tkinter as tk
from tkinter import messagebox
from baseDeDatos import BaseDeDatos

class VentanaCuentas(tk.Tk, BaseDeDatos):
    def __init__(self):
        super().__init__()

        # Instancia BD
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
        # Evaluar que las dos contrasenas sean iguales
        if self.contrasena_entry.get() != self.contrasena2_entry.get():
            messagebox.showerror("Error", "Las contrasenas no coinciden")
        else:
            try:
                # Credenciales ingresadas
                usuario = self.usuario_entry.get()
                contrasena = self.contrasena2_entry.get()
                # Base de datos
                conexion = self.mysql.conexion()
                if conexion is True:
                    # Aplicar hash a contrasena
                    bool_hash, contrasena_hash, salt_hash = self.mysql.hash(contrasena.encode("utf-8"), None)
                    if bool_hash is True:
                        guardar_cuenta = self.mysql.ejecutar_consulta("INSERT INTO cuentas(usuario, contrasena, salt) VALUES(%s, %s, %s)", (usuario, contrasena_hash, salt_hash))
                        if guardar_cuenta is True:
                            messagebox.showinfo("Aviso", "Cuenta generada con exito")
                            self.mysql.cerrar_conexion()
                        else:
                            messagebox.showerror("Error en la consulta", guardar_cuenta)
                    else:
                        messagebox.showerror("Error de hash", bool_hash)
                else:
                    messagebox.showerror("Error de conexion", conexion)
                
            except Exception as e:
                messagebox.showwarning(None, e)



if __name__ == '__main__':
    app = VentanaCuentas()
    app.mainloop()