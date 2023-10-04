import sqlite3
import hashlib
import os

def crear_tabla_usuarios():
    conn = sqlite3.connect("mi_base_de_datos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT NOT NULL,
            salt TEXT NOT NULL,
            hash_contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def registrar_usuario(nombre_usuario, contrasena):
    salt = os.urandom(16)
    hash_contrasena = hashlib.pbkdf2_hmac('sha256', contrasena.encode('utf-8'), salt, 100000)
    
    conn = sqlite3.connect("mi_base_de_datos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre_usuario, salt, hash_contrasena) VALUES (?, ?, ?)",
                   (nombre_usuario, salt, hash_contrasena.hex()))
    conn.commit()
    conn.close()

def verificar_credenciales(nombre_usuario, contrasena):
    conn = sqlite3.connect("mi_base_de_datos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT salt, hash_contrasena FROM usuarios WHERE nombre_usuario=?", (nombre_usuario,))
    resultado = cursor.fetchone()
    
    if resultado:
        salt = resultado[0]
        hash_contrasena_guardada = resultado[1]
        hash_contrasena = hashlib.pbkdf2_hmac('sha256', contrasena.encode('utf-8'), salt, 100000).hex()
        
        if hash_contrasena == hash_contrasena_guardada:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Nombre de usuario no encontrado.")
    
    conn.close()

# Ejemplo de uso
crear_tabla_usuarios()
registrar_usuario("usuario1", "contrasena1")

nombre_usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")
verificar_credenciales(nombre_usuario, contrasena)
