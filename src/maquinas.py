import sqlite3

DB_PATH = "taller.db"  # Cambia el nombre si usas otro

def crear_maquina(nombre, modelo, fecha_adquisicion):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO maquinas (nombre, modelo, fecha_adquisicion)
        VALUES (?, ?, ?)
    """, (nombre, modelo, fecha_adquisicion))
    conn.commit()
    conn.close()

def buscar_maquina(maquina_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maquinas WHERE id = ?", (maquina_id,))
    maquina = cursor.fetchone()
    conn.close()
    return maquina

def eliminar_maquina(maquina_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM maquinas WHERE id = ?", (maquina_id,))
    conn.commit()
    conn.close()

def modificar_maquina(maquina_id, nombre, modelo, fecha_adquisicion):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE maquinas
        SET nombre = ?, modelo = ?, fecha_adquisicion = ?
        WHERE id = ?
    """, (nombre, modelo, fecha_adquisicion, maquina_id))
    conn.commit()
    conn.close()

def listar_maquinas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maquinas")
    maquinas = cursor.fetchall()
    conn.close()
    return maquinas
