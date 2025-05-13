import sqlite3

DB_PATH = "taller.db"  # Podés cambiarlo si usás otro nombre

def crear_cliente(nombre, apellido, telefono, email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (nombre, apellido, telefono, email)
        VALUES (?, ?, ?, ?)
    """, (nombre, apellido, telefono, email))
    conn.commit()
    conn.close()

def buscar_cliente(cliente_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

def eliminar_cliente(cliente_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()

def modificar_cliente(cliente_id, nombre, apellido, telefono, email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clientes
        SET nombre = ?, apellido = ?, telefono = ?, email = ?
        WHERE id = ?
    """, (nombre, apellido, telefono, email, cliente_id))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes
