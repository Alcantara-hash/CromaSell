import tkinter as tk
from tkinter import messagebox
from baseDeDatos2 import BaseDeDatos

class ventanaConexionBD(tk.Tk):
    def __init__(self):

        super().__init__()

        self.title("Acceso")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        # Widgets de la ventana

        host_label = tk.Label(self, text= "Host: ")
        host_label.pack()

        self.host_entry = tk.Entry(self)
        self.host_entry.pack()

        user_label = tk.Label(self, text= "User: ")
        user_label.pack()

        self.user_entry = tk.Entry(self)
        self.user_entry.pack()

        password_label = tk.Label(self, text= "Password: ")
        password_label.pack()

        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        Database_label = tk.Label(self, text= "Database: ")
        Database_label.pack()

        self.database_entry = tk.Entry(self)
        self.database_entry.pack()

        conexion_button = tk.Button(self, text= "Conectar", command= self.conexion)
        conexion_button.pack()
    
    def conexion(self):
        try:
            bd = BaseDeDatos(self.host_entry.get(), self.user_entry.get(), self.password_entry.get(), self.database_entry.get())
        except Exception as error:
            messagebox.showerror("!Error¡", "No se logro la conexíon con la Base de Datos.\n{error}")
        else:
            messagebox.showinfo("Aviso", "Conexion establecida.")
            bd.cerrar_conexion()


if __name__ == '__main__':
    app = ventanaConexionBD()
    app.mainloop()