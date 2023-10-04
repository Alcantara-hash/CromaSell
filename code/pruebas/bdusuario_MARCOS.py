import tkinter as tk
from tkinter import PhotoImage, messagebox
import mysql.connector
from PIL import Image, ImageTk

def verificar_credenciales():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    global fondo 
    try:
        # Intentar conectar a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto al usuario correcto
            password="12345678",  # Cambia esto a la contraseña correcta
            database="inicio_de_sesion")

        cursor = conexion.cursor()

        # Consulta SQL para verificar las credenciales
        consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
        parametros = (usuario, contrasena)

        cursor.execute(consulta, parametros)
        resultado = cursor.fetchone()

        # Cerrar la conexión a la base de datos
        cursor.close()
        conexion.close()

        # Verificar si las credenciales son correctas
        if resultado:
            ventana.withdraw()  # Ocultar la ventana de inicio de sesión
            abrir_nueva_ventana(usuario)

        else:
            mensaje_error.config(text="Credenciales incorrectas. Por favor, inténtalo de nuevo.")

    except mysql.connector.Error as error:
        # Manejar errores de conexión a la base de datos
        messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos: " + str(error))

def abrir_nueva_ventana(usuario):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Interfaz Principal")
    nueva_ventana.geometry("1366x768")

    label_usuario = tk.Label(nueva_ventana, text="Usuario: " + usuario)
    label_usuario.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    global fondo  # Declarar fondo como una variable global
    try:
        fondo = PhotoImage(file="img/fondo_m.png")
        fondo_label = tk.Label(nueva_ventana, image=fondo)
        fondo_label.place(relwidth=1, relheight=1)
    except Exception as e:
        print("Error al cargar la imagen de fondo:", str(e))
        fondo = None

    # Función para abrir una nueva página
    def abrir_pagina_nueva():
        nueva_pagina = tk.Toplevel()
        nueva_pagina.title("Nueva Página")

        # Puedes personalizar la nueva página aquí

    # Agregar 4 botones en la nueva ventana utilizando grid
    boton1 = tk.Button(nueva_ventana, text="INVENTARIO", width=20, height=5, command=abrir_pagina_nueva)  # Modificar tamaño del botón 1
    boton2 = tk.Button(nueva_ventana, text="CONSULTAR VENTAS", width=20, height=5)
    boton3 = tk.Button(nueva_ventana, text="BUSCAR ARTICULO", width=20, height=5)
    boton4 = tk.Button(nueva_ventana, text="VER RECIBO", width=20, height=5)

    # Posicionar los botones en la esquina inferior
    boton1.grid(row=2, column=0, padx=10, pady=10)
    boton2.grid(row=3, column=0, padx=10, pady=10)
    boton3.grid(row=4, column=0, padx=10, pady=10)
    boton4.grid(row=5, column=0, padx=10, pady=10)
    # Puedes configurar las funciones para cada botón aquí, si es necesario

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Establecer el tamaño de la ventana a 764x764
ventana.resizable(False, False)
ventana.geometry("764x650")

# Cargar la imagen de fondo (debe estar dentro del bloque try)
try:
    fondo = PhotoImage(file="img/fondo_n.png")  # Cambia el nombre de la imagen y la ruta según corresponda
    fondo_label = tk.Label(ventana, image=fondo)
    fondo_label.place(relwidth=1, relheight=1)
except Exception as e:
    print("Error al cargar la imagen de fondo:", str(e))
    fondo = None

# Crear etiquetas
#usuario_entry = tk.Entry(ventana, font=("Helvetica", 15))  # Modificar la fuente y el tamaño según sea necesario
#contrasena_entry = tk.Entry(ventana, show="*", font=("Helvetica", 15))  # Modificar la fuente y el tamaño según sea necesario

# Crear campos de entrada
usuario_entry = tk.Entry(ventana, font=("Helvetica", 15))  # Modificar la fuente y el tamaño según sea necesario
contrasena_entry = tk.Entry(ventana, show="*", font=("Helvetica", 15))  # Modificar la fuente y el tamaño según sea necesario

# Crear botón de inicio de sesión y modificar posición y tamaño
inicio_sesion_button = tk.Button(ventana, text="INICIAR SESION", command=verificar_credenciales, font=("Arial", 12, "bold"), width=150, height=50)
# Utiliza el método grid para configurar la posición y tamaño del botón
try:
    boton_imagen = Image.open("img/BOTONL.png")
    boton_imagen = ImageTk.PhotoImage(boton_imagen)
    inicio_sesion_button.config(image=boton_imagen)  # Coloca la imagen a la izquierda del texto del botón
    inicio_sesion_button.image = boton_imagen  # Guarda una referencia para evitar que la imagen se elimine
except Exception as e:
    print("Error al cargar la imagen del botón:", str(e))


# Crear mensaje de error
mensaje_error = tk.Label(ventana, text="", fg="red")

# Texto superpuesto sin fondo
#texto_usuario = tk.Text(ventana, height=1, width=10, font=("ARIAL", 15), bg=ventana.cget("bg"))
#texto_usuario.insert(tk.END, "USUARIO")
#texto_usuario.config(state="disabled", bd=0, highlightthickness=0, relief=tk.FLAT)
#texto_usuario.tag_configure("center", justify="center")
#texto_usuario.tag_add("center", "1.0", "end")
#texto_usuario.place(relx=0.570, rely=0.475, anchor="e")

#texto_contrasena = tk.Text(ventana, height=1, width=15, font=("ARIAL", 15), bg=ventana.cget("bg"))
#texto_contrasena.insert(tk.END, "CONTRASEÑA")
#texto_contrasena.config(state="disabled", bd=0, highlightthickness=0, relief=tk.FLAT)
#texto_contrasena.tag_configure("center", justify="center")
#texto_contrasena.tag_add("center", "1.0", "end")
#texto_contrasena.place(relx=0.60, rely=0.60, anchor="e")


# Centrar los elementos en la posición (329, 240) dentro de la ventana de 764x1080
usuario_entry.place(relx=0.340, rely=0.52, anchor="w")
contrasena_entry.place(relx=0.345, rely=0.63, anchor="w")
inicio_sesion_button.place(relx=0.38, rely=0.74, anchor="w")
mensaje_error.place(relx=0.5, rely=0.85, anchor="center")

# Ejecutar la aplicación
ventana.mainloop()