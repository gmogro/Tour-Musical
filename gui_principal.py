from Servicios.servicio_ubicacion import ServicioUbicacion
import tkinter as tk
from tkinter import ttk

serv_ubicacion = ServicioUbicacion()

def guardar():
    serv_ubicacion.finalizar()
    
def crearUbicacion():
    nombre = entry_nombre_ubicacion.get()
    direccion = entry_direccion.get()
    coordenas = []
    coordenas.append(entry_latitud.get())
    coordenas.append(entry_longitud.get())
    serv_ubicacion.crearUbicacion(nombre,direccion,coordenas)

root = tk.Tk()
root.title("Tour Musical")
root.geometry("800x800")

frame = ttk.Frame(root)
frame.grid(row=0,rowspan=2,column=0,columnspan=2,padx=10,pady=10)

# Crear etiqueta de nombre de Ubicacion
label_nombre_ubicacion = ttk.Label(frame, text="Nombre Ubicacion:")
label_nombre_ubicacion.grid(row=0, column=0, padx=10, pady=10)

# Crear entrada de nombre de Ubicacion
entry_nombre_ubicacion = tk.Entry(frame)
entry_nombre_ubicacion.grid(row=0, column=1, padx=10, pady=10)

# Crear etiqueta de nombre de Direccion
label_direccion = ttk.Label(frame, text="Nombre Direccion:")
label_direccion.grid(row=1, column=0, padx=10, pady=10)

# Crear entrada de nombre de Direccion
entry_direccion = tk.Entry(frame)
entry_direccion.grid(row=1, column=1, padx=10, pady=10)

# Crear etiqueta de nombre de Coordenadas
label_latitud = ttk.Label(frame, text="Latitud:")
label_latitud.grid(row=2, column=0, padx=10, pady=10)

# Crear entrada de nombre de Coordenas
entry_latitud = tk.Entry(frame)
entry_latitud.grid(row=2, column=1, padx=10, pady=10)

# Crear etiqueta de nombre de Coordenadas
label_longitud = ttk.Label(frame, text="Longitud: ")
label_longitud.grid(row=3, column=0, padx=10, pady=10)

# Crear entrada de nombre de Coordenadas
entry_longitud = tk.Entry(frame)
entry_longitud.grid(row=3, column=1, padx=10, pady=10)

# Crear botón de Crear Ubicacion
button_create = tk.Button(frame, text="Crear Ubicacion",command = crearUbicacion )
button_create.grid(row=4, columnspan=4, padx=10, pady=10)

# Crear botón de Crear Ubicacion
button_guardar = tk.Button(frame, text="Guardar",command = guardar )
button_guardar.grid(row=5, columnspan=2, padx=10, pady=10)


root.mainloop()

