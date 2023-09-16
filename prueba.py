import tkinter as tk
import random

# Definir el tamaño del tablero
filas = 15
columnas = 15

# Crear el tablero
tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Colocar el robot en una posición aleatoria
robot_fila = random.randint(0, filas - 1)
robot_columna = random.randint(0, columnas - 1)
tablero[robot_fila][robot_columna] = 'R'

# Colocar robots enemigos en posiciones aleatorias
num_robots_enemigos = 5
enemigos = []

for _ in range(num_robots_enemigos):
    while True:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = 'E'
            enemigos.append((fila, columna))
            break

# Colocar el objetivo en una posición aleatoria
objetivo_fila = random.randint(0, filas - 1)
objetivo_columna = random.randint(0, columnas - 1)
tablero[objetivo_fila][objetivo_columna] = 'O'

# Función para mostrar el tablero en la ventana
def mostrar_tablero():
    for i in range(filas):
        for j in range(columnas):
            label = tk.Label(root, text=tablero[i][j], width=4, height=2)
            label.grid(row=i, column=j)

# Función para mover al robot y a los enemigos
def mover(event):
    global robot_fila, robot_columna
    key = event.keysym
    tablero[robot_fila][robot_columna] = ' '
    if key == 'w' and robot_fila > 0:
        robot_fila -= 1
    elif key == 's' and robot_fila < filas - 1:
        robot_fila += 1
    elif key == 'a' and robot_columna > 0:
        robot_columna -= 1
    elif key == 'd' and robot_columna < columnas - 1:
        robot_columna += 1
    elif key == 'q' and robot_fila > 0 and robot_columna > 0:
        robot_fila -= 1
        robot_columna -= 1
    elif key == 'e' and robot_fila > 0 and robot_columna < columnas - 1:
        robot_fila -= 1
        robot_columna += 1
    elif key == 'z' and robot_fila < filas - 1 and robot_columna > 0:
        robot_fila += 1
        robot_columna -= 1
    elif key == 'c' and robot_fila < filas - 1 and robot_columna < columnas - 1:
        robot_fila += 1
        robot_columna += 1
    tablero[robot_fila][robot_columna] = 'R'
    eliminar_enemigos()
    if (robot_fila, robot_columna) in enemigos:
        mostrar_tablero()
        perder_juego()
    mover_enemigos()
    mostrar_tablero()

# Función para eliminar enemigos que estén uno al lado del otro
def eliminar_enemigos():
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
            tablero[objetivo_fila][objetivo_columna] = 'O'
            enemigos[i] = (objetivo_fila, objetivo_columna)

# Función para indicar que el jugador ha perdido
def perder_juego():
    perder_window = tk.Toplevel(root)
    perder_window.title("¡Perdiste!")
    perder_label = tk.Label(perder_window, text="Tocaste a un enemigo. ¡Has perdido!")
    perder_label.pack()
    perder_button = tk.Button(perder_window, text="Cerrar", command=perder_window.destroy)
    perder_button.pack()

# Configurar la ventana principal
root = tk.Tk()
root.title("Juego Robots")

# Mostrar el tablero inicial
mostrar_tablero()

# Enlazar el evento de teclado para mover al robot
root.bind("<Key>", mover)

# Iniciar la interfaz gráfica
root.mainloop()
