import pyodbc
from tkinter import *
from tkinter import messagebox

# Conexión a la base de datos SQL Server
conexion = pyodbc.connect(
    'DRIVER={SQL SERVER};'
    'SERVER=LAPTOP-35TF4KBD\\SQLEXPRESS;'
    'DATABASE=granja_ucundinamarca;'
    'Trusted_Connection=yes;'
)
cursor = conexion.cursor()


# Función para agregar un nuevo cultivo
def agregar_cultivo():
    nombre = nombre_entry.get()
    tipo = tipo_entry.get()
    area_cultivo = int(area_cultivo_entry.get())
    rendimiento = int(rendimiento_entry.get())

    cursor.execute('INSERT INTO cultivos (nombre, tipo, area_cultivo, rendimiento) VALUES (?, ?, ?, ?)',
                   (nombre, tipo, area_cultivo, rendimiento))
    conexion.commit()
    messagebox.showinfo("Éxito", f"Cultivo '{nombre}' agregado exitosamente!")


# Función para consultar todos los cultivos
def consultar_cultivos():
    cursor.execute('SELECT * FROM cultivos')
    cultivos = cursor.fetchall()
    for cultivo in cultivos:
        print(cultivo)


# Función para modificar un cultivo existente
def modificar_cultivo():
    id_cultivo = int(id_cultivo_entry.get())
    nombre = nombre_entry.get()
    tipo = tipo_entry.get()
    area_cultivo = int(area_cultivo_entry.get())
    rendimiento = int(rendimiento_entry.get())

    cursor.execute('UPDATE cultivos SET nombre = ?, tipo = ?, area_cultivo = ?, rendimiento = ? WHERE id = ?',
                   (nombre, tipo, area_cultivo, rendimiento, id_cultivo))
    conexion.commit()
    messagebox.showinfo("Éxito", f"Cultivo con ID {id_cultivo} modificado exitosamente!")


# Función para eliminar un cultivo
def eliminar_cultivo():
    id_cultivo = int(id_cultivo_entry.get())

    cursor.execute('DELETE FROM cultivos WHERE id = ?', (id_cultivo,))
    conexion.commit()
    messagebox.showinfo("Éxito", f"Cultivo con ID {id_cultivo} eliminado exitosamente!")


# Función para agregar un nuevo animal
def agregar_animal():
    especie = especie_entry.get()
    raza = raza_entry.get()
    edad = int(edad_entry.get())
    peso = int(peso_entry.get())

    cursor.execute('INSERT INTO animales (especie, raza, edad, peso) VALUES (?, ?, ?, ?)',
                   (especie, raza, edad, peso))
    conexion.commit()
    messagebox.showinfo("Éxito", f"Animal '{especie}' agregado exitosamente!")


# Función para consultar todos los animales
def consultar_animales():
    cursor.execute('SELECT * FROM animales')
    animales = cursor.fetchall()
    for animal in animales:
        print(animal)


# Función para modificar un animal existente
def modificar_animal():
    id_animal = int(id_animal_entry.get())
    especie = especie_entry.get()
    raza = raza_entry.get()
    edad = int(edad_entry.get())
    peso = int(peso_entry.get())

    cursor.execute('UPDATE animales SET especie = ?, raza = ?, edad = ?, peso = ? WHERE id = ?',
                   (especie, raza, edad, peso, id_animal))
    conexion.commit()
    messagebox.showinfo("Éxito", f"Animal con ID {id_animal} modificado exitosamente!")


# Función para eliminar un animal
def eliminar_animal():
    id_animal = int(id_animal_entry.get())

    cursor.execute('DELETE FROM animales WHERE id = ?', (id_animal,))
    conexion.commit()
    messagebox.showinfo("Éxito", f"Animal con ID {id_animal} eliminado exitosamente!")


# Función para calcular la producción total de cultivos
def calcular_produccion_total_cultivos():
    cursor.execute('SELECT SUM(rendimiento * area_cultivo) FROM cultivos')
    produccion_total = cursor.fetchone()[0]
    messagebox.showinfo("Producción total de cultivos", f"Producción total de cultivos: {produccion_total} kg")


# Función para calcular la producción total del ganado (si aplica)
def calcular_produccion_total_ganado():
    cursor.execute('SELECT SUM(peso) AS TotalPeso FROM animales')
    produccion_total = cursor.fetchone()[0]
    messagebox.showinfo("Producción total del ganado", f"Producción total del ganado: {produccion_total} kg")


# Función para calcular la producción total de la granja
def calcular_produccion_total_granja():
    produccion_total_cultivos = calcular_produccion_total_cultivos()
    produccion_total_ganado = calcular_produccion_total_ganado()
    produccion_total = produccion_total_cultivos + produccion_total_ganado
    messagebox.showinfo("Producción total de la granja", f"Producción total de la granja: {produccion_total} kg")


# Función para generar un reporte de producción
def generar_reporte_produccion_total():
    calcular_produccion_total_granja()


# Interfaz gráfica
root = Tk()
root.title("Sistema de Gestión de Granja")
root.geometry("400x500")

# Etiquetas
Label(root, text="ID Cultivo:").grid(row=0, column=0)
Label(root, text="Nombre:").grid(row=1, column=0)
Label(root, text="Tipo:").grid(row=2, column=0)
Label(root, text="Área de cultivo:").grid(row=3, column=0)
Label(root, text="Rendimiento:").grid(row=4, column=0)

Label(root, text="ID Animal:").grid(row=0, column=2)
Label(root, text="Especie:").grid(row=1, column=2)
Label(root, text="Raza:").grid(row=2, column=2)
Label(root, text="Edad:").grid(row=3, column=2)
Label(root, text="Peso:").grid(row=4, column=2)

# Entradas
id_cultivo_entry = Entry(root)
id_cultivo_entry.grid(row=0, column=1)
nombre_entry = Entry(root)
nombre_entry.grid(row=1, column=1)
tipo_entry = Entry(root)
tipo_entry.grid(row=2, column=1)
area_cultivo_entry = Entry(root)
area_cultivo_entry.grid(row=3, column=1)
rendimiento_entry = Entry(root)
rendimiento_entry.grid(row=4, column=1)

id_animal_entry = Entry(root)
id_animal_entry.grid(row=0, column=3)
especie_entry = Entry(root)
especie_entry.grid(row=1, column=3)
raza_entry = Entry(root)
raza_entry.grid(row=2, column=3)
edad_entry = Entry(root)
edad_entry.grid(row=3, column=3)
peso_entry = Entry(root)
peso_entry.grid(row=4, column=3)

# Botones
Button(root, text="Agregar Cultivo", command=agregar_cultivo).grid(row=5, column=0, columnspan=2, pady=10)
Button(root, text="Consultar Cultivos", command=consultar_cultivos).grid(row=5, column=2, columnspan=2, pady=10)

Button(root, text="Modificar Cultivo", command=modificar_cultivo).grid(row=6, column=0, columnspan=2, pady=10)
Button(root, text="Eliminar Cultivo", command=eliminar_cultivo).grid(row=6, column=2, columnspan=2, pady=10)

Button(root, text="Agregar Animal", command=agregar_animal).grid(row=7, column=0, columnspan=2, pady=10)
Button(root, text="Consultar Animales", command=consultar_animales).grid(row=7, column=2, columnspan=2, pady=10)

Button(root, text="Modificar Animal", command=modificar_animal).grid(row=8, column=0, columnspan=2, pady=10)
Button(root, text="Eliminar Animal", command=eliminar_animal).grid(row=8, column=2, columnspan=2, pady=10)

Button(root, text="Calcular Producción Total de Cultivos", command=calcular_produccion_total_cultivos).grid(row=9, column=0, columnspan=4, pady=10)
Button(root, text="Calcular Producción Total del Ganado", command=calcular_produccion_total_ganado).grid(row=10, column=0, columnspan=4, pady=10)
Button(root, text="Calcular Producción Total de la Granja", command=calcular_produccion_total_granja).grid(row=11, column=0, columnspan=4, pady=10)
Button(root, text="Generar Reporte de Producción Total", command=generar_reporte_produccion_total).grid(row=12, column=0, columnspan=4, pady=10)

root.mainloop()

# Cerrar la conexión a la base de datos
conexion.close()
