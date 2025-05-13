import os
import sqlite3

# Asegurarse de que exista la carpeta 'database' antes de crear la DB
os.makedirs("database", exist_ok=True)

# Ruta de la base de datos
DB_PATH = "database/taller.db"

# Conexión a la base de datos
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Ejecutar el script SQL que crea las tablas
with open("scripts/crear_tablas.sql", "r", encoding="utf-8") as f:
    cursor.executescript(f.read())

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
