import mysql.connector
from mysql.connector import errorcode
import json
import hashlib
import os

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
    def __init__(self, host, user, password, database):
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

        self.cursor = self.connection.cursor()

    def ejecutar_consulta(self, query, values= None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True        
        except mysql.connector.Error as error:
            self.connection.rollback()
            return False
    
    def obtener_datos(self, query, values= None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
    
    def obtener_error(self):
        return self.errores
    
    def hash(self, contrasena):
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

        return hash_contrasena



if __name__ == '__main__':

    archivo_JSON = archivo_JSON()
    archivo_JSON.crear_JSON("127.0.0.1", "root", "", "cromasell")

    host, user, password, database = archivo_JSON.leer_JSON()
    print(user)

    # Conexion al BD
    bd = BaseDeDatos(host, user, password, database)
    bd.agregar_cuenta("Tadeo", "12345hola")
    bd.cerrar_conexion()