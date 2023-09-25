import tkinter as tk
import pygame

pygame.init()


# Ventana seleccion de personaje
def wnd_juego():
    
    wnd_menu.destroy()  
    juego = tk.Tk()
    juego.title("Juego")
    juego.minsize(height=600, width=1200)


    slider_volumen2 = tk.Scale(juego, from_=100, to=0, orient="vertical", command=actualizar_volumen, bg=("dark red"), fg="white",  )
    slider_volumen2.set(50)  # Establecer el valor inicial del volumen al 50%
    slider_volumen2.place(x=1160, y=0)
    
    
    # Guardar nombre del jugador
    def guardar_en_archivo():
        nomb = entrada.get()
        with open("usuarios.txt", "w") as archivo:
            archivo.write([0,nomb])

    # Fondo seleccion de personaje  
    lbl_juego_fondo = tk.Label(juego,bg="dark red", width=1200, height=600)
    lbl_juego_fondo.place(x=0, y=0)  
      
    ajedrez = tk.PhotoImage(file="ajedrez.png")
    lbl_juego_fondo = tk.Label(juego, image=ajedrez, border=False)
    lbl_juego_fondo.place(x=300, y=0)  
    

    btn_cerrarJUEGO = tk.Button(juego, command=juego.destroy,  font=("Arial", 20), bg=("dark red"),fg="white" , text="Salir")
    btn_cerrarJUEGO.place(x=1050, y= 500)

    # Nombre de usuario
    Nombre = tk.Label(juego, text="Nombre del jugador", fg="Black", font="Arial, 15", bg="#920202")
    Nombre.place(y=40, x=920)

    entrada = tk.Entry(juego, width=20, font=("Arial, 15"),  fg="white", bg="black" )
    entrada.place(y=75, x=920)

    
    juego.mainloop()

# Ventana información personal
def wnd_info():
    info_per = tk.Toplevel()
    info_per.title("Información")
    info_per.minsize(height=600, width=1200)

    # Fondo informacion        
    infor = tk.PhotoImage(file="datos.png")
    lbl_inf = tk.Label(info_per, image=infor)
    lbl_inf.place(x=0, y=0)    

    btn_cerrarinfo = tk.Button(info_per, command=info_per.destroy,  font=("Arial", 20), bg=("dark red"),fg="white" , text="Volver")
    btn_cerrarinfo.place(x=1050, y= 500)

    img_yo = tk.PhotoImage(file="daniel.png")
    lbl_yo = tk.Label(info_per, image=img_yo,)
    lbl_yo.place(x=700, y=200)

    info_per.mainloop()

# Ventana de clasificaciones
def wnd_rankeds():
    rankeds = tk.Tk()
    rankeds.title("Tabla de puntaciones")
    rankeds.minsize(height=600, width=1200)
    

    lbl_fondoranked = tk.Label(rankeds, bg="#571919", width=1200, height=600)
    lbl_fondoranked.place(x=0, y=0)

    btn_cerrarranked = tk.Button(rankeds, command=rankeds.destroy,  font=("Arial", 20), bg=("dark red"),fg="white" , text="Volver")
    btn_cerrarranked.place(x=1050, y= 500)


    def cargar_archivo():
        with open( "usuarios.txt", 'r') as archivo:
            contenido = archivo.read()
            label.config(text=contenido)

    label = tk.Label(rankeds, text="", wraplength=400, bg="dark red", fg="white", font=("Arial", 20) )
    label.place(x=400, y=150)

    titu_rankds = tk.Label(rankeds, text="Tabla de clasificaciones:", bg="dark red", fg="white", font=("Arial", 20))
    titu_rankds.place(x=430, y=50)

    cargar_archivo()

    rankeds.mainloop

# Ventana principal
wnd_menu = tk.Tk()
wnd_menu.title("Inicio")
# Fondo menú principal
doom = tk.PhotoImage(file="doom.png")
lbl_fondo = tk.Label(wnd_menu, image=doom)
lbl_fondo.pack()

# Música
pygame.mixer.music.load("rolita.mp3")
pygame.mixer.music.play(-1)

def actualizar_volumen(valor):
    volumen = float(valor) / 100.0
    pygame.mixer.music.set_volume(volumen)

# Slider para configurar el volumen de la música
slider_volumen = tk.Scale(wnd_menu, from_=100, to=0, orient="vertical", command=actualizar_volumen, bg=("dark red"), fg="white",  )
slider_volumen.set(50)  # Establecer el valor inicial del volumen al 50%
slider_volumen.place(x=1160, y=0)

# Botón Para selecionar personaje
btn_juego = tk.Button(wnd_menu, text="JUGAR", command=wnd_juego, font=("Arial", 20), bg=("dark red"),fg="white" )
btn_juego.place(x=530, y=500)

# Botón para información del programa
btn_info = tk.Button(wnd_menu, text="INFO", command=wnd_info, font=("Arial", 20), bg=("dark red"),fg="white" )
btn_info.place(x=420, y=500)

# Botón para información del programa
btn_rankeds = tk.Button(wnd_menu, text="RANKED", command=wnd_rankeds, font=("Arial", 20), bg=("dark red"),fg="white" )
btn_rankeds.place(x=670, y=500)


wnd_menu.mainloop()