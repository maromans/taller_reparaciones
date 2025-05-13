import sqlite3
import os
import tkinter as tk
from tkinter import messagebox
from clientes import crear_cliente, buscar_cliente, eliminar_cliente, modificar_cliente, listar_clientes
from maquinas import crear_maquina, buscar_maquina, eliminar_maquina, modificar_maquina, listar_maquinas
from reparaciones import crear_reparacion, buscar_reparacion, eliminar_reparacion, modificar_reparacion, listar_reparaciones

# Ruta de la base de datos en la raíz del proyecto
DB_PATH = "../src/taller.db"

# Ruta del script SQL
SQL_SCRIPT_PATH = "../src/crear_tablas.sql"

def crear_base_de_datos():
    if os.path.exists(SQL_SCRIPT_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        with open(SQL_SCRIPT_PATH, "r", encoding="utf-8") as f:
            cursor.executescript(f.read())
        conn.commit()
        conn.close()
        print("Base de datos creada correctamente.")
    else:
        print(f"No se encontró el archivo SQL en: {SQL_SCRIPT_PATH}")

crear_base_de_datos()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión del Taller")
        self.root.geometry("600x400")
        self.main_menu()

    def main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Menú Principal", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Gestionar Clientes", command=self.menu_clientes).pack(pady=10)
        tk.Button(self.root, text="Gestionar Máquinas", command=self.menu_maquinas).pack(pady=10)
        tk.Button(self.root, text="Gestionar Reparaciones", command=self.menu_reparaciones).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def agregar_boton_volver(self):
        tk.Button(self.root, text="Volver al Menú Principal", command=self.main_menu).pack(pady=20)

    # ========================= CLIENTES =========================
    def menu_clientes(self):
        self.clear_window()

        tk.Label(self.root, text="Gestión de Clientes", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Crear Cliente", command=self.crear_cliente_gui).pack(pady=5)
        tk.Button(self.root, text="Listar Clientes", command=self.listar_clientes_gui).pack(pady=5)
        tk.Button(self.root, text="Buscar Cliente", command=self.buscar_cliente_gui).pack(pady=5)
        tk.Button(self.root, text="Eliminar Cliente", command=self.eliminar_cliente_gui).pack(pady=5)
        tk.Button(self.root, text="Modificar Cliente", command=self.modificar_cliente_gui).pack(pady=5)

        self.agregar_boton_volver()

    def crear_cliente_gui(self):
        self.clear_window()
        tk.Label(self.root, text="Crear Cliente", font=("Arial", 14)).pack(pady=10)

        campos = ["Nombre", "Apellido", "Teléfono", "Email"]
        entradas = {}
        for campo in campos:
            tk.Label(self.root, text=f"{campo}:").pack()
            entrada = tk.Entry(self.root)
            entrada.pack()
            entradas[campo.lower()] = entrada

        tk.Button(
            self.root,
            text="Crear",
            command=lambda: self.crear_cliente(
                entradas["nombre"].get(),
                entradas["apellido"].get(),
                entradas["teléfono"].get(),
                entradas["email"].get()
            )
        ).pack(pady=10)

        self.agregar_boton_volver()

    def crear_cliente(self, nombre, apellido, telefono, email):
        crear_cliente(nombre, apellido, telefono, email)
        messagebox.showinfo("Éxito", "Cliente creado correctamente")
        self.menu_clientes()

    def listar_clientes_gui(self):
        self.clear_window()
        tk.Label(self.root, text="Listado de Clientes", font=("Arial", 14)).pack(pady=10)
        for cliente in listar_clientes():
            tk.Label(self.root, text=str(cliente)).pack()

        self.agregar_boton_volver()

    def buscar_cliente_gui(self):
        self.clear_window()
        tk.Label(self.root, text="Buscar Cliente", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="ID Cliente:").pack()
        entry_id = tk.Entry(self.root)
        entry_id.pack()

        tk.Button(self.root, text="Buscar", command=lambda: self.buscar_cliente(entry_id.get())).pack(pady=10)
        self.agregar_boton_volver()

    def buscar_cliente(self, cliente_id):
        cliente = buscar_cliente(cliente_id)
        if cliente:
            messagebox.showinfo("Cliente Encontrado", f"Cliente: {cliente}")
        else:
            messagebox.showerror("Error", "Cliente no encontrado")
        self.menu_clientes()

    def eliminar_cliente_gui(self):
        self.clear_window()
        tk.Label(self.root, text="Eliminar Cliente", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="ID Cliente:").pack()
        entry_id = tk.Entry(self.root)
        entry_id.pack()

        tk.Button(self.root, text="Eliminar", command=lambda: self.eliminar_cliente(entry_id.get())).pack(pady=10)
        self.agregar_boton_volver()

    def eliminar_cliente(self, cliente_id):
        eliminar_cliente(cliente_id)
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        self.menu_clientes()

    def modificar_cliente_gui(self):
        self.clear_window()
        tk.Label(self.root, text="Modificar Cliente", font=("Arial", 14)).pack(pady=10)

        campos = ["ID Cliente", "Nuevo Nombre", "Nuevo Apellido", "Nuevo Teléfono", "Nuevo Email"]
        entradas = {}
        for campo in campos:
            tk.Label(self.root, text=f"{campo}:").pack()
            entrada = tk.Entry(self.root)
            entrada.pack()
            entradas[campo.lower()] = entrada

        tk.Button(
            self.root,
            text="Modificar",
            command=lambda: self.modificar_cliente(
                entradas["id cliente"].get(),
                entradas["nuevo nombre"].get(),
                entradas["nuevo apellido"].get(),
                entradas["nuevo teléfono"].get(),
                entradas["nuevo email"].get()
            )
        ).pack(pady=10)

        self.agregar_boton_volver()

    def modificar_cliente(self, cliente_id, nombre, apellido, telefono, email):
        modificar_cliente(cliente_id, nombre, apellido, telefono, email)
        messagebox.showinfo("Éxito", "Cliente modificado correctamente")
        self.menu_clientes()

    # ========================= MÁQUINAS =========================
    def menu_maquinas(self):
        self.clear_window()
        tk.Label(self.root, text="Gestión de Máquinas", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Crear Máquina", command=self.crear_maquina_gui).pack(pady=5)
        tk.Button(self.root, text="Listar Máquinas", command=self.listar_maquinas_gui).pack(pady=5)
        tk.Button(self.root, text="Buscar Máquina", command=self.buscar_maquina_gui).pack(pady=5)
        tk.Button(self.root, text="Eliminar Máquina", command=self.eliminar_maquina_gui).pack(pady=5)
        tk.Button(self.root, text="Modificar Máquina", command=self.modificar_maquina_gui).pack(pady=5)

        self.agregar_boton_volver()

    def crear_maquina_gui(self):
        self.clear_window()
        # Implementar formulario similar al de cliente
        # ...
        self.agregar_boton_volver()

    def listar_maquinas_gui(self):
        self.clear_window()
        for maquina in listar_maquinas():
            tk.Label(self.root, text=str(maquina)).pack()
        self.agregar_boton_volver()

    def buscar_maquina_gui(self):
        self.clear_window()
        # Similar a buscar_cliente_gui
        self.agregar_boton_volver()

    def eliminar_maquina_gui(self):
        self.clear_window()
        # Similar a eliminar_cliente_gui
        self.agregar_boton_volver()

    def modificar_maquina_gui(self):
        self.clear_window()
        # Similar a modificar_cliente_gui
        self.agregar_boton_volver()

    # ========================= REPARACIONES =========================
    def menu_reparaciones(self):
        self.clear_window()
        tk.Label(self.root, text="Gestión de Reparaciones", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Crear Reparación", command=self.crear_reparacion_gui).pack(pady=5)
        tk.Button(self.root, text="Listar Reparaciones", command=self.listar_reparaciones_gui).pack(pady=5)
        tk.Button(self.root, text="Buscar Reparación", command=self.buscar_reparacion_gui).pack(pady=5)
        tk.Button(self.root, text="Eliminar Reparación", command=self.eliminar_reparacion_gui).pack(pady=5)
        tk.Button(self.root, text="Modificar Reparación", command=self.modificar_reparacion_gui).pack(pady=5)

        self.agregar_boton_volver()

    def crear_reparacion_gui(self):
        self.clear_window()
        # Implementar formulario
        self.agregar_boton_volver()

    def listar_reparaciones_gui(self):
        self.clear_window()
        for reparacion in listar_reparaciones():
            tk.Label(self.root, text=str(reparacion)).pack()
        self.agregar_boton_volver()

    def buscar_reparacion_gui(self):
        self.clear_window()
        # Similar a buscar_cliente_gui
        self.agregar_boton_volver()

    def eliminar_reparacion_gui(self):
        self.clear_window()
        # Similar a eliminar_cliente_gui
        self.agregar_boton_volver()

    def modificar_reparacion_gui(self):
        self.clear_window()
        # Similar a modificar_cliente_gui
        self.agregar_boton_volver()


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
