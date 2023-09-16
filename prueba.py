import pygame
import tkinter as tk
from tkinter import ttk

# Función para actualizar el volumen según el valor del slider
def actualizar_volumen(valor):
    volumen = float(valor) / 100.0
    pygame.mixer.music.set_volume(volumen)

# Inicializar Pygame
pygame.init()

# Crear una ventana de Pygame (no se mostrará)
pygame.display.set_mode((200, 200))

# Cargar el archivo de audio
pygame.mixer.music.load("rolita.mp3")

# Configurar la reproducción en bucle
pygame.mixer.music.play(-1)

# Crear la ventana de la aplicación GUI
ventana = tk.Tk()
ventana.title("Control de Volumen")

# Crear un slider para el volumen
slider_volumen = ttk.Scale(ventana, from_=0, to=100, orient="horizontal", command=actualizar_volumen)
slider_volumen.set(50)  # Establecer el valor inicial del volumen al 50%
slider_volumen.pack(padx=20, pady=20)

# Mantener la ventana de la aplicación en funcionamiento
ventana.mainloop()

# Cuando hayas terminado, asegúrate de cerrar Pygame
pygame.quit()