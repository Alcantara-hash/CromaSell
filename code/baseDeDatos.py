# Cambiar la conexion de BD Local, a Cliente - Servidor.
import sqlite3
import hashlib
import os

class BaseDeDatos:
    def __init__(self):

        self.conn = sqlite3.connect("cromasell_BD")
        self.cursor = self.conn.cursor()

    def crear_tablas(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS usuarios (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                usuario TEXT NOT NULL,
                                salt TEXT NOT NULL,
                                contrasena TEXT NOT NULL
                            )
                            ''')
        self.conn.commit()

    def agregar_usuarios(self, usuario, contrasena):

        """
        El "salt" (sal) es una cadena aleatoria que se genera para cada usuario y se combina con su contraseña antes de 
        aplicar la función de derivación de clave (PBKDF2). Esto añade una capa adicional de seguridad a las contraseñas
        almacenadas en la base de datos.
        """
        # Salt aleatorio, lo que crea una cadena de 16 bytes (128 bits) de entropía aleatoria.
        salt = os.urandom(16)
        """
        PBKDF2 es una función criptográfica que se utiliza para derivar una clave secreta a partir de una contraseña y un salt.
        """
        """
        En el código, se utiliza hashlib.pbkdf2_hmac para aplicar PBKDF2 con el algoritmo de hash SHA-256 y 100,000 iteraciones. 
        Esto significa que el proceso se realiza 100,000 veces para aumentar la seguridad.
        """
        hash_contrasena = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), salt, 10000)
        # Ademas de todo el encriptado, el resultado se pasa a Base16.
        hash_contrasena.hex()

        self.cursor.execute("INSERT INTO usuarios(usuario, salt, contrasena) VALUES(?, ?, ?)", (usuario, salt, hash_contrasena))
        self.conn.commit()
    
    def obtener_todos_los_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        self.conn.close()

if __name__ == '__main__':

    bd = BaseDeDatos()
    #bd.crear_tablas()

    """
    """
    #bd.agregar_usuarios("rebeca", "hola 123")
    """
    """
    print("Todos los usuarios: ")
    usuarios = bd.obtener_todos_los_usuarios()
    for usuario in usuarios:
        print(usuario)

    """
    bd.cursor.execute("INSERT INTO usuarios (nombre, apellido, edad) VALUES (?, ?, ?)",("John", "Doe", 30))
    bd.conn.commit()
    """
    
    bd.cerrar_conexion()
