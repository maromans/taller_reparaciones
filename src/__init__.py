"""Taller de Reparaciones - Módulo de Base de Datos
Este módulo contiene funciones para conectar a la base de datos 
SQLite y crear las tablas necesarias para el sistema de gestión de reparaciones.
"""
import sqlite3

def conectar():
    conn = sqlite3.connect('taller.db')
    return conn

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            telefono TEXT,
            direccion TEXT,
            email TEXT,
            fecha_registro DATE DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maquinas (
            id_maquina INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            marca TEXT,
            modelo TEXT,
            descripcion TEXT,
            FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reparaciones (
            id_reparacion INTEGER PRIMARY KEY AUTOINCREMENT,
            id_maquina INTEGER,
            fecha_ingreso DEFAULT CURRENT_TIMESTAMP,
            fecha_entrega TEXT,
            descripcion_trabajo TEXT,
            costo REAL,
            FOREIGN KEY(id_maquina) REFERENCES maquinas(id_maquina)
        )
    ''')
    conn.commit()
    conn.close()
