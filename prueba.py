import tkinter as tk
import random
import pygame


# Sonido al disparar
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("escopeta.mp3") 
    pygame.mixer.music.set_volume(0.1)  # Establece el volumen actual
    pygame.mixer.music.play()

# Definir el tamaño del tablero
filas = 15
columnas = 15

# Crear el tablero
tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Colocar el jugador en una posición aleatoria
robot_fila = random.randint(0, filas - 1)
robot_columna = random.randint(0, columnas - 1)
tablero[robot_fila][robot_columna] = 'R'

# Variables
num_robots_enemigos = 10
bombas_iniciales = 4
disparos_iniciales = 20
enemigos = []
puntos = 0
bombas = bombas_iniciales
disparos = disparos_iniciales

# Función para colocar robots enemigos en posiciones aleatorias
for _ in range(num_robots_enemigos):
    while True:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = 'E'
            enemigos.append((fila, columna))
            break

# Función para mostrar el tablero en la ventana
def mostrar_tablero():
    for i in range(filas):
        for j in range(columnas):
            label = tk.Label(root, text=tablero[i][j], width=4, height=2)
            label.grid(row=i, column=j)

# Función para mover al robot y a los enemigos, disparar, dejar bombas y teletransportarse
def mover(event):
    movimiento=False
    disparo=False
    global robot_fila, robot_columna, puntos, tablero, bombas, disparos, disparos_iniciales, bombas_iniciales
    key = event.keysym
    # Movimiento
    if tablero[robot_fila][robot_columna]!="O":
        tablero[robot_fila][robot_columna] = ' '
    if key == 'w' and robot_fila > 0:
        robot_fila -= 1
        movimiento=True
    elif key == 'w' and robot_fila == 0:
        robot_fila = 14
        movimiento=True
    elif key == 's' and robot_fila < filas - 1:
        robot_fila += 1
        movimiento=True
    elif key == 's' and robot_fila == filas - 1:
        robot_fila = 0
        movimiento=True
    elif key == 'a' and robot_columna > 0:
        robot_columna -= 1
        movimiento=True
    elif key == 'a' and robot_columna == 0:
        robot_columna = 14
        movimiento=True
    elif key == 'd' and robot_columna < columnas - 1:
        robot_columna += 1
        movimiento=True
    elif key == 'd' and robot_columna == columnas - 1:
        robot_columna = 0
        movimiento=True
    elif key == 'q' and robot_fila > 0 and robot_columna > 0:
        robot_fila -= 1
        robot_columna -= 1
        movimiento=True
    elif key == 'q' and robot_fila == 0 and robot_columna == 0:
        robot_fila = 14
        robot_columna = 14
        movimiento=True
    elif key == 'e' and robot_fila > 0 and robot_columna < columnas - 1:
        robot_fila -= 1
        robot_columna += 1
        movimiento=True
    elif key == 'e' and robot_fila == 0 and robot_columna == columnas - 1:
        robot_fila = 14
        robot_columna = 0
        movimiento=True
    elif key == 'z' and robot_fila < filas - 1 and robot_columna > 0:
        robot_fila += 1
        robot_columna -= 1
        movimiento=True
    elif key == 'z' and robot_fila == filas - 1 and robot_columna == 0:
        robot_fila = 0
        robot_columna = 14
        movimiento=True
    elif key == 'c' and robot_fila < filas - 1 and robot_columna < columnas - 1:
        robot_fila += 1
        robot_columna += 1
        movimiento=True
    elif key == 'c' and robot_fila == filas - 1 and robot_columna == columnas - 1:
        robot_fila = 0
        robot_columna = 0
        movimiento=True
    # Disparos
    elif key == 'u':
        play_sound()
        if tablero[pos(robot_fila,-1)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,-1),robot_columna)
            
        elif tablero[pos(robot_fila,-2)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,-2),robot_columna)
            
        else:
            disparos -=1 
        disparo=True
    elif key == 'j':
        play_sound()
        if tablero[pos(robot_fila,1)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,1),robot_columna)
        elif tablero[pos(robot_fila,2)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,2),robot_columna)
        else:
            disparos -=1 
        disparo=True
    elif key == 'h':
        play_sound()
        if tablero[robot_fila][pos(robot_columna,-1)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,-1))
        elif tablero[robot_fila][pos(robot_columna,-2)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,-2))
        else:
            disparos -=1    
        disparo=True
    elif key == 'k':
        play_sound()
        if tablero[robot_fila][pos(robot_columna,1)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,1))
        elif tablero[robot_fila][pos(robot_columna,2)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,2))
        else:
            disparos -=1    
        disparo=True
    elif key == 'y':
        play_sound()
        if tablero[pos(robot_fila,-1)][pos(robot_columna,-1)]== 'E':
            eliminar_enemigos(pos(robot_fila,-1),pos(robot_columna,-1))
        elif tablero[pos(robot_fila,-2)][pos(robot_columna,-2)]== 'E':
            eliminar_enemigos(pos(robot_fila,-2),pos(robot_columna,-2))
        else:
            disparos -=1
        disparo=True
    elif key == 'i':
        play_sound()
        if tablero[pos(robot_fila,-1)][pos(robot_columna,1)]== 'E':
            eliminar_enemigos(pos(robot_fila,-1),pos(robot_columna,1))
        elif tablero[pos(robot_fila,-2)][pos(robot_columna,2)]== 'E':
            eliminar_enemigos(pos(robot_fila,-2),pos(robot_columna,2))
        else:
            disparos -=1
        disparo=True
    elif key == 'n':
        play_sound()
        if tablero[pos(robot_fila,1)][pos(robot_columna,-1)]== 'E':
            eliminar_enemigos(pos(robot_fila,1),pos(robot_columna,-1))
        elif tablero[pos(robot_fila,2)][pos(robot_columna,-2)]== 'E':
            eliminar_enemigos(pos(robot_fila,2),pos(robot_columna,-2))
        else:
            disparos -=1
        disparo=True
    elif key == 'm':
        play_sound()
        if tablero[pos(robot_fila,1)][pos(robot_columna,1)]== 'E':
            eliminar_enemigos(pos(robot_fila,1),pos(robot_columna,1))
        elif tablero[pos(robot_fila,2)][pos(robot_columna,2)]== 'E':
            eliminar_enemigos(pos(robot_fila,2),pos(robot_columna,2))
        else:
            disparos -=1
        disparo=True
    # Bomba
    elif key=="b":
        play_sound()
        if bombas!=0:
            tablero[robot_fila][robot_columna] = 'O'
            bombas -=1

    # Teletransportes
    elif key=="t":  #Random
        if puntos > 5:
            robot_fila = random.randint(0, filas - 1)
            robot_columna = random.randint(0, columnas - 1)
            if tablero[robot_fila][robot_columna]=="E":
                perder_juego()
            elif tablero[robot_fila][robot_columna]=="X":
                perder_juego()
            else:
                disparo=True
            puntos -= 5
    elif key=="g":  #Segura
        if puntos > 25:
            while(True):
                robot_fila = random.randint(0, filas - 1)
                robot_columna = random.randint(0, columnas - 1)
                if tablero[robot_fila][robot_columna]==' ' and tablero[pos(robot_fila,-1)][robot_columna]==' ' and tablero[pos(robot_fila,1)][robot_columna]==' ' and tablero[robot_fila][pos(robot_columna,-1)] == ' ' and tablero[robot_fila][pos(robot_columna,1)] == ' ' and tablero[pos(robot_fila,-1)][pos(robot_columna,-1)]== ' ' and tablero[pos(robot_fila,-1)][pos(robot_columna,1)]== ' ' and tablero[pos(robot_fila,1)][pos(robot_columna,-1)]== ' ' and tablero[pos(robot_fila,1)][pos(robot_columna,1)]== ' ':
                    break
                puntos -= 25
                disparo=True
    # Movimiento de los enemigos
    if enemigos==[]:
        bombas=bombas_iniciales+1
        disparos=disparos_iniciales
        for _ in range(num_robots_enemigos+5):
            while True:
                fila = random.randint(0, filas - 1)
                columna = random.randint(0, columnas - 1)
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = 'E'
                    enemigos.append((fila, columna))
                    break
        
    
    # Función para actualizar el tablero    
    if movimiento:
        tablero[robot_fila][robot_columna] = 'R'
        eliminar_enemigos(0,0)
        if (robot_fila, robot_columna) in enemigos:
            mostrar_tablero()
            perder_juego()
    
        puntos += 5
        mover_enemigos()
        mostrar_tablero()
        print(puntos,bombas,disparos)
        return tablero
    if disparo:
        tablero[robot_fila][robot_columna] = 'R'
        eliminar_enemigos(0,0)
        mostrar_tablero()
        print(puntos,bombas,disparos)
        return tablero
        

# Función para la posición
def pos(actual, incremento):
    if actual==13 and incremento == 2:
        return 0
    elif actual==14 and incremento == 1:
        return 0
    elif actual==14 and incremento == 2:
        return 1
    elif actual==0 and incremento == -1:
        return 14
    elif actual==0 and incremento == -2:
        return 13
    elif actual == 1 and incremento == -2:
        return 14
    else:
        return actual+incremento


# Función para eliminar enemigos que estén uno al lado del otro
def eliminar_enemigos(a,b):
    global  puntos, disparos
    ban=False
    if a!=0 and b!=0:
        ban=True
    i = 0
    while i < len(enemigos) - 1:
        fila1, columna1 = enemigos[i]
        fila2, columna2 = enemigos[i + 1]
        if abs(fila1 - fila2) + abs(columna1 - columna2) == 1:
            tablero[fila1][columna1] = 'X'
            tablero[fila2][columna2] = 'X'
            del enemigos[i]
            del enemigos[i]  # Eliminar el segundo enemigo
        else:
            i += 1
    for j in range(len(enemigos)-1):
        fila, columna = enemigos[j]
        if a==fila and b==columna:
            del enemigos[j]
            tablero[a][b] = ' '
            ban=False
            puntos += 10
            disparos -=1
    if ban:
        enemigos.pop()
        tablero[a][b] = ' '
        puntos += 10
        disparos -=1
        
            
# Función para mover a los enemigos un lugar en una dirección aleatoria
def mover_enemigos():
    for i, (fila, columna) in enumerate(enemigos):
        direccion = random.choice(['w', 's', 'a', 'd', 'q', 'e', 'z', 'c'])
        nueva_fila, nueva_columna = fila, columna

        if direccion == 'w' and fila > 0:
            nueva_fila -= 1
        elif direccion == 's' and fila < filas - 1:
            nueva_fila += 1
        elif direccion == 'a' and columna > 0:
            nueva_columna -= 1
        elif direccion == 'd' and columna < columnas - 1:
            nueva_columna += 1
        elif direccion == 'q' and fila > 0 and columna > 0:
            nueva_fila -= 1
            nueva_columna -= 1
        elif direccion == 'e' and fila > 0 and columna < columnas - 1:
            nueva_fila -= 1
            nueva_columna += 1
        elif direccion == 'z' and fila < filas - 1 and columna > 0:
            nueva_fila += 1
            nueva_columna -= 1
        elif direccion == 'c' and fila < filas - 1 and columna < columnas - 1:
            nueva_fila += 1
            nueva_columna += 1

        if tablero[nueva_fila][nueva_columna] == ' ':
            tablero[fila][columna] = ' '
            tablero[nueva_fila][nueva_columna] = 'E'
            enemigos[i] = (nueva_fila, nueva_columna)
        elif tablero[nueva_fila][nueva_columna] == 'O':
            # Si un enemigo llega al objetivo, se reinicia su posición
            tablero[fila][columna] = ' '
            tablero[nueva_fila][nueva_columna] = ' '
            del enemigos[i]

# Función para indicar que el jugador ha perdido
def perder_juego():
    global  puntos, nombre
    perder_window = tk.Toplevel(root)
    perder_window.title("¡Perdiste!")
    perder_label = tk.Label(perder_window, text="Tocaste a un enemigo. ¡Has perdido!")
    perder_label.pack()
    perder_button = tk.Button(perder_window, text="Cerrar", command=perder_window.destroy)
    perder_button.pack()

    entrada = tk.Entry(perder_window, width=20, font=("Arial, 15"),  fg="white", bg="black" )
    entrada.pack()
    nombre = entrada.get()

    resultado=[puntos,nombre]
    resultados=lector()
    resultados=resultados+[resultado]
    resultados=ordenar(resultados)
    escritor(resultados)
    print(nombre)


# Agregar texto al txt "usuarios"
def ordenar(matriz):
    return sorted(matriz, key=lambda x: x[0], reverse=True)

def lector():
    
    with open('usuarios.txt', 'r') as archivo:
        datos = []
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) >= 2:
                numero = int(partes[0])
                nombre = partes[1]
                datos.append([numero, nombre])

    return datos

def escritor(lista):
    with open('usuarios.txt', 'w') as archivo:
        for dato in lista:
            linea = ','.join(map(str, dato))
            archivo.write(linea + '\n')


# Configurar la ventana principal
root = tk.Tk()
root.title("Juego Robots")


# Mostrar el tablero inicial
mostrar_tablero()

# Enlazar el evento de teclado para mover al robot
root.bind("<Key>", mover)

# Iniciar la interfaz gráfica
root.mainloop()
