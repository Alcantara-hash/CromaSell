import mysql.connector
import json
import bcrypt

class archivo_JSON():
    def __init__(self):
        self.error = None

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
        self.connection = None
        self.cursor = None

    def conexion(self):
        try:
            # Instancia archivo_JSON()
            credenciales_bd = archivo_JSON()
            host, user, password, database = credenciales_bd.leer_JSON() # Extraer credenciales

            # Crear conexión
            self.connection = mysql.connector.connect(
                host = host,
                user = user, 
                password = password, 
                database = database
                )
            
            # Crear cursor
            self.cursor = self.connection.cursor()
            return True
        
        except mysql.connector.Error as e:
            self.error = e
            return self.error

    
    def cerrar_conexion(self):
        try:
            self.cursor.close()
            self.connection.close()
            return True
        except mysql.connector.Error as e:
            return e

    def crear_BD():

        DB_NAME = "cromasell"
        TABLES = {}

        TABLES["cuentas"] = (
            "CREATE TABLE cuentas("
            "ID int(11) NOT NULL AUTO_INCREMENT,"
            "usuario VARCHAR(20) NOT NULL,"
            "contrasena VARCHAR(150) NOT NULL,"
            "salt VARCHAR(30) NOT NULL,"
            "PRIMARY KEY(ID)"
            ") ENGINE=InnoDB"
        )

        
    def ejecutar_consulta(self, query, values= None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        
        except mysql.connector.Error as e:
            return e
    
    def obtener_datos(self, query, values= None):
        try:
            self.cursor.execute(query, values)
            datos = self.cursor.fetchall()
            return True, datos

        except mysql.connector.Error as e:
            return False, e
    
    def hash(self, contrasena = None, salt_in = None):
        try:
            # salt
            if salt_in is None:
                salt = bcrypt.gensalt()
                contrasena_hash = bcrypt.hashpw(contrasena, salt)
                return True, contrasena_hash, salt
            else:
                salt = salt_in
                contrasena_hash = bcrypt.hashpw(contrasena, salt)
                return True, contrasena_hash
        
        except Exception as e:
            return False, e

if __name__ == "__main__":
    pass