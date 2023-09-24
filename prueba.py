import tkinter as tk
import random

# Definir el tamaño del tablero
filas = 15
columnas = 15

#puntos
puntos=0

# Crear el tablero
tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Colocar el robot en una posición aleatoria
robot_fila = random.randint(0, filas - 1)
robot_columna = random.randint(0, columnas - 1)
tablero[robot_fila][robot_columna] = 'R'

# Colocar robots enemigos en posiciones aleatorias
num_robots_enemigos = 10
enemigos = []

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

# Función para mover al robot y a los enemigos
def mover(event):
    movimiento=False
    disparo=False
    global robot_fila, robot_columna, puntos, tablero
    key = event.keysym
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
    elif key == 'u':
        if tablero[pos(robot_fila,-1)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,-1),robot_columna)
            
        elif tablero[pos(robot_fila,-2)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,-2),robot_columna)
            
        else:
            print("logica de disparos") 
        disparo=True
    elif key == 'j':
        if tablero[pos(robot_fila,1)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,1),robot_columna)
        elif tablero[pos(robot_fila,2)][robot_columna]=='E':
            eliminar_enemigos(pos(robot_fila,2),robot_columna)
        else:
            print("logica de disparos") 
        disparo=True
    elif key == 'h':
        if tablero[robot_fila][pos(robot_columna,-1)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,-1))
        elif tablero[robot_fila][pos(robot_columna,-2)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,-2))
        else:
            print("logica de disparos")    
        disparo=True
    elif key == 'k':
        if tablero[robot_fila][pos(robot_columna,1)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,1))
        elif tablero[robot_fila][pos(robot_columna,2)] == 'E':
            eliminar_enemigos(robot_fila,pos(robot_columna,2))
        else:
            print("logica de disparos")    
        disparo=True
    elif key == 'y':
        if tablero[pos(robot_fila,-1)][pos(robot_columna,-1)]== 'E':
            eliminar_enemigos(pos(robot_fila,-1),pos(robot_columna,-1))
        elif tablero[pos(robot_fila,-2)][pos(robot_columna,-2)]== 'E':
            eliminar_enemigos(pos(robot_fila,-2),pos(robot_columna,-2))
        else:
            print("logica de disparos")
        disparo=True
    elif key == 'i':
        if tablero[pos(robot_fila,-1)][pos(robot_columna,1)]== 'E':
            eliminar_enemigos(pos(robot_fila,-1),pos(robot_columna,1))
        elif tablero[pos(robot_fila,-2)][pos(robot_columna,2)]== 'E':
            eliminar_enemigos(pos(robot_fila,-2),pos(robot_columna,2))
        else:
            print("logica de disparos")
        disparo=True
    elif key == 'n':
        if tablero[pos(robot_fila,1)][pos(robot_columna,-1)]== 'E':
            eliminar_enemigos(pos(robot_fila,1),pos(robot_columna,-1))
        elif tablero[pos(robot_fila,2)][pos(robot_columna,-2)]== 'E':
            eliminar_enemigos(pos(robot_fila,2),pos(robot_columna,-2))
        else:
            print("logica de disparos")
        disparo=True
    elif key == 'm':
        if tablero[pos(robot_fila,1)][pos(robot_columna,1)]== 'E':
            eliminar_enemigos(pos(robot_fila,1),pos(robot_columna,1))
        elif tablero[pos(robot_fila,2)][pos(robot_columna,2)]== 'E':
            eliminar_enemigos(pos(robot_fila,2),pos(robot_columna,2))
        else:
            print("logica de disparos")
        disparo=True
    elif key=="b":
        tablero[robot_fila][robot_columna] = 'O'
        
    elif key=="t":
        robot_fila = random.randint(0, filas - 1)
        robot_columna = random.randint(0, columnas - 1)
        if tablero[robot_fila][robot_columna]=="E":
            perder_juego()
        elif tablero[robot_fila][robot_columna]=="X":
            perder_juego()
        else:
            disparo=True
            
    elif key=="g":
        while(True):
            robot_fila = random.randint(0, filas - 1)
            robot_columna = random.randint(0, columnas - 1)
            if tablero[robot_fila][robot_columna]==' ' and tablero[pos(robot_fila,-1)][robot_columna]==' ' and tablero[pos(robot_fila,1)][robot_columna]==' ' and tablero[robot_fila][pos(robot_columna,-1)] == ' ' and tablero[robot_fila][pos(robot_columna,1)] == ' ' and tablero[pos(robot_fila,-1)][pos(robot_columna,-1)]== ' ' and tablero[pos(robot_fila,-1)][pos(robot_columna,1)]== ' ' and tablero[pos(robot_fila,1)][pos(robot_columna,-1)]== ' ' and tablero[pos(robot_fila,1)][pos(robot_columna,1)]== ' ':
                break
            disparo=True
        
        
    if movimiento:
        tablero[robot_fila][robot_columna] = 'R'
        eliminar_enemigos(0,0)
        if (robot_fila, robot_columna) in enemigos:
            mostrar_tablero()
            perder_juego()
    
        puntos += 5
        mover_enemigos()
        mostrar_tablero()
        return tablero
    if disparo:
        tablero[robot_fila][robot_columna] = 'R'
        eliminar_enemigos(0,0)
        mostrar_tablero()
        return tablero
        
        
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
    if ban:
        enemigos.pop()
        tablero[a][b] = ' '
        
            
        

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