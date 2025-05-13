import sqlite3

DB_PATH = "taller.db"  # Cambia el nombre si usas otro

def crear_reparacion(maquina_id, descripcion, fecha_reparacion, costo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reparaciones (maquina_id, descripcion, fecha_reparacion, costo)
        VALUES (?, ?, ?, ?)
    """, (maquina_id, descripcion, fecha_reparacion, costo))
    conn.commit()
    conn.close()

def buscar_reparacion(reparacion_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reparaciones WHERE id = ?", (reparacion_id,))
    reparacion = cursor.fetchone()
    conn.close()
    return reparacion

def eliminar_reparacion(reparacion_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reparaciones WHERE id = ?", (reparacion_id,))
    conn.commit()
    conn.close()

def modificar_reparacion(reparacion_id, maquina_id, descripcion, fecha_reparacion, costo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reparaciones
        SET maquina_id = ?, descripcion = ?, fecha_reparacion = ?, costo = ?
        WHERE id = ?
    """, (maquina_id, descripcion, fecha_reparacion, costo, reparacion_id))
    conn.commit()
    conn.close()

def listar_reparaciones():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reparaciones")
    reparaciones = cursor.fetchall()
    conn.close()
    return reparaciones
