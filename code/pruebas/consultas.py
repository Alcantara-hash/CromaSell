import sqlite3 as bd

conn = bd.connect("cromasell_BD")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
resultado = cursor.fetchall()

for usuario in resultado:
    print(usuario)

conn.close()