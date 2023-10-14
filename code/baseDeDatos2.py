import mysql.connector

class BaseDeDatos():
    def __init__(self, host, user, password, database):
        # Conexión a la BD
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        self.cursor = self.connection.cursor()

    def ejecutar_consulta(self, query, values= None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        
        except mysql.connector.Error as error:
            # messagebox.showinfo("")
            self.connection.rollback()
            return False
    
    def obtener_datos(self, query, values= None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()