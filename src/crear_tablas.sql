-- Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    telefono TEXT,
    email TEXT
);

-- Tabla de máquinas
CREATE TABLE IF NOT EXISTS maquinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    marca TEXT,
    modelo TEXT,
    numero_serie TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Tabla de reparaciones
CREATE TABLE IF NOT EXISTS reparaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    maquina_id INTEGER NOT NULL,
    fecha_ingreso TEXT NOT NULL,
    fecha_egreso TEXT,
    descripcion TEXT,
    costo REAL,
    FOREIGN KEY (maquina_id) REFERENCES maquinas(id)
);
