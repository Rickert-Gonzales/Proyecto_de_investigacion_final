# Importacion de librerias
from tkinter import *
from tkinter import filedialog
import os

window = Tk()
window.title("Sistema de analisis de rendimiento")  # Cambiar el nombre de la ventana
window.geometry("520x480")  # Configurar tamaño
window.iconbitmap("figure.ico")  # Cambiar el icono


# Funcion de carga de archivos
def cargar_archivo():
    archivo_guardado = filedialog.asksaveasfilename(initialdir="/",
                                                    title="Selecciona archivo",
                                                    defaultextension=".cvs",
                                                    filetypes=(("all files", "*.*"),
                                                               ("txt files", "*.txt")))
    archivo = open(archivo_guardado, "w")
    print(archivo_guardado)


# Creacion del boton de carga
Button(text="Guardar archivo", bg="light green", command=cargar_archivo).place(x=32, y=24)

# Mostrar Ventana
window.mainloop()
