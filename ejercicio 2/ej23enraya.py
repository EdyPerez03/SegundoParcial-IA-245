import random

def generar_aleatorio(min_val, max_val, semilla):
    semilla = (semilla * 9301 + 49297) % 233280
    aleatorio = min_val + (semilla / 233280) * (max_val - min_val)
    return aleatorio, semilla

def inicializar_pesos(filas, columnas, semilla):
    pesos = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            aleatorio, semilla = generar_aleatorio(-1, 1, semilla)
            fila.append(aleatorio)
        pesos.append(fila)
    return pesos, semilla

def inicializar_sesgos(cantidad, semilla):
    sesgos = []
    for i in range(cantidad):
        aleatorio, semilla = generar_aleatorio(-1, 1, semilla)
        sesgos.append(aleatorio)
    return sesgos, semilla

def relu(x):
    return max(0, x)

def calcular_salida(tablero, pesos_oculta, sesgos_oculta, pesos_salida, sesgos_salida):
    capa_oculta = []
    for i in range(len(pesos_oculta)):
        suma = sum(tablero[j] * pesos_oculta[i][j] for j in range(len(tablero))) + sesgos_oculta[i]
        capa_oculta.append(relu(suma))
    
    salida = []
    for i in range(len(pesos_salida)):
        suma = sum(capa_oculta[j] * pesos_salida[i][j] for j in range(len(capa_oculta))) + sesgos_salida[i]
        salida.append(suma)
    return salida, capa_oculta

def hacer_jugada(tablero, salida, jugador):
    mejor_jugada = salida.index(max(salida))
    
    if tablero[mejor_jugada] == 0:
        tablero[mejor_jugada] = jugador
        return True
    else:
        posiciones_vacias = [i for i, val in enumerate(tablero) if val == 0]
        if posiciones_vacias:
            jugada_aleatoria = random.choice(posiciones_vacias)
            tablero[jugada_aleatoria] = jugador
            return True
        else:
            return False

def verificar_ganador(tablero):
    combinaciones_victoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]                
    ]
    
    for combinacion in combinaciones_victoria:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] != 0:
            return True  
    
    if all(c != 0 for c in tablero): 
        return True
    
    return False  

def mostrar_tablero(tablero):
    for i in range(0, 9, 3):
        print(tablero[i:i+3])

def entrenar_red(tablero, resultado, pesos_oculta, sesgos_oculta, pesos_salida, sesgos_salida, tasa_aprendizaje=0.1):
    if resultado == 1:
        recompensa = 1
    elif resultado == -1:
        recompensa = -1
    else:
        recompensa = 0  
    
    for i in range(len(pesos_salida)):
        for j in range(len(pesos_salida[i])):
            pesos_salida[i][j] += tasa_aprendizaje * recompensa  
    return pesos_oculta, sesgos_oculta, pesos_salida, sesgos_salida

def jugar(tablero, semilla):
    global n  
    semilla_maquina = semilla
    semilla_rival = semilla + 1

    pesos_oculta_maquina, semilla_maquina = inicializar_pesos(10, 9, semilla_maquina)
    sesgos_oculta_maquina, semilla_maquina = inicializar_sesgos(10, semilla_maquina)
    pesos_salida_maquina, semilla_maquina = inicializar_pesos(9, 10, semilla_maquina)
    sesgos_salida_maquina, semilla_maquina = inicializar_sesgos(9, semilla_maquina)

    pesos_oculta_rival, semilla_rival = inicializar_pesos(10, 9, semilla_rival)
    sesgos_oculta_rival, semilla_rival = inicializar_sesgos(10, semilla_rival)
    pesos_salida_rival, semilla_rival = inicializar_pesos(9, 10, semilla_rival)
    sesgos_salida_rival, semilla_rival = inicializar_sesgos(9, semilla_rival)

    while n > 0 and any(c == 0 for c in tablero):  
        salida_maquina, capa_oculta_maquina = calcular_salida(tablero, pesos_oculta_maquina, sesgos_oculta_maquina, pesos_salida_maquina, sesgos_salida_maquina)
        if hacer_jugada(tablero, salida_maquina, 1):
            n -= 1
            mostrar_tablero(tablero)
            if verificar_ganador(tablero):
                print("¡La máquina ganó!")
                entrenar_red(tablero, 1, pesos_oculta_maquina, sesgos_oculta_maquina, pesos_salida_maquina, sesgos_salida_maquina)  
                break
        else:
            print("La máquina no pudo hacer una jugada válida.")
            break

        salida_rival, capa_oculta_rival = calcular_salida(tablero, pesos_oculta_rival, sesgos_oculta_rival, pesos_salida_rival, sesgos_salida_rival)
        if hacer_jugada(tablero, salida_rival, -1):
            n -= 1
            mostrar_tablero(tablero)
            if verificar_ganador(tablero):
                print("¡El rival ganó!")
                entrenar_red(tablero, -1, pesos_oculta_rival, sesgos_oculta_rival, pesos_salida_rival, sesgos_salida_rival)  
                break
        else:
            print("El rival no pudo hacer una jugada válida.")
            break

    if n == 0 and not verificar_ganador(tablero):
        print("¡Empate!")

n = 9
tablero = [0] * 9
semilla = 12345
jugar(tablero, semilla)
