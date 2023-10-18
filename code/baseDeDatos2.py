import mysql.connector
from mysql.connector import errorcode
import json
import hashlib
import os
from tkinter import messagebox as msj

class archivo_JSON():
    def __init__(self):
        pass

    def crear_JSON(self, host, user, password, database):
        datos_JSON = {
            "host":host,
            "user":user,
            "password":password,
            "database":database
        }
        try:
            with open("config.json", "w") as archivo_JSON:
                json.dump(datos_JSON, archivo_JSON)
        except PermissionError:
            print("No tienes los permisos para guardar el archivo.")
        except OSError as e:
            print(f"Error al guardar el archivo JSON: {e}")

    def leer_JSON(self):
        with open("config.json", "r") as archivo_JSON:
            datos_JSON = json.load(archivo_JSON)
        
        host = datos_JSON["host"]
        user = datos_JSON["user"]
        password = datos_JSON["password"]
        database = datos_JSON["database"]

        return  host, user, password, database

    def actualizar_JSON(self):
        pass



class BaseDeDatos():
    def __init__(self):
        """
        try:
            self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
            )
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.errores = error
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                self.errores = error
            else:
                self.errores = error
        """
        #self.connection = mysql.connector.connect()
        #self.cursor = self.connection.cursor()
    
    def conexion(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as error:
            return f"Tipo de error: {error}"

    def ejecutar_consulta(self, query, values= None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True        
        except mysql.connector.Error as error:
            self.connection.rollback()
            return False, error
    
    def obtener_datos(self, query, values= None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            return error
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
    
    def obtener_error(self):
        return self.errores
    
    def hash(self, contrasena, salt):
        """
        PBKDF2 es una función criptográfica que se utiliza para derivar una clave secreta a partir de una contraseña y un salt.
        """
        """ 
        En el código, se utiliza hashlib.pbkdf2_hmac para aplicar PBKDF2 con el algoritmo de hash SHA-256 y 100,000 iteraciones. 
        Esto significa que el proceso se realiza 100,000 veces para aumentar la seguridad.
        """
        # Salt aleatorio, lo que crea una cadena de 16 bytes (128 bits) de entropía aleatoria.
        #salt = os.urandom(16)
        #guardar_salt = salt

        # Aplicacion del Hash
        try:
            hash_contrasena = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), salt, 10000)
            return hash_contrasena
        except Exception as error:
            return f"Tipo de error: {error}"
        # Ademas de todo el encriptado, el resultado se pasa a Base16.
        #hash_contrasena.hex()



if __name__ == '__main__':

    archivo_JSON = archivo_JSON()
    host, user, password, database = archivo_JSON.leer_JSON()

    db = BaseDeDatos()
    db.conexion(host, user, password, database)

    # Agregar cuenta
    usuario = "admin"
    contrasena = "root1"
    salt = os.urandom(16)

    contrasena_hasheada = db.hash(contrasena, salt)

    agregar_cuenta = db.ejecutar_consulta("INSERT INTO cuentas(usuario, contrasena, salt) VALUES(%s, %s, %s,)", (usuario, contrasena_hasheada, salt))

    if isinstance(agregar_cuenta, str):
        msj.showerror("error", agregar_cuenta)
    else:
        msj.showinfo("aviso", "cuenta guardada")

    #credenciales_bd = db.obtener_datos("SELECT salt FROM cuentas WHERE usuario = %s and contrasena = %s", (user, contrasena, salt))


    db.hash()

    db.cerrar_conexion()