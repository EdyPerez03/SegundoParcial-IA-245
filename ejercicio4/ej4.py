import random

grafo = {
    'A': {'B': 7, 'C': 9, 'D': 10},
    'B': {'A': 7, 'C': 8, 'D': 4},
    'C': {'A': 9, 'B': 8, 'E': 5},
    'D': {'A': 10, 'B': 4, 'E': 17},
    'E': {'C': 5, 'D': 17}
}

nodos = ['A', 'B', 'C', 'D', 'E']
nodo_inicio = 'A'

#ruleta rusa

nodos_excluyendo_A = [nodo for nodo in nodos if nodo != 'A']
nodo_final = random.choice(nodos_excluyendo_A)


print("Nodo inicio: ", nodo_inicio, " Nodo final: ", nodo_final)
tam_poblacion = 10
generaciones = 100

#Anotación de Edy: Aquí si se quiere entrenar para solo un camino se reemplaza la ruleta rusa por una variable llamada nodo_final = "el nodo específico"#


def random_path(grafo, nodos, inicio, fin):
    nodos_intermedios = [n for n in nodos if n != inicio and n != fin]
    random.shuffle(nodos_intermedios)
    return [inicio] + nodos_intermedios + [fin]

def fitness(path):
    distancia_total = 0
    for i in range(len(path) - 1):
      
        if path[i + 1] not in grafo[path[i]]:
            return float('inf')  
        distancia_total += grafo[path[i]][path[i + 1]]
    return 1 / distancia_total if distancia_total > 0 else float('inf')

def crossover(padre1, padre2):
    split = random.randint(1, len(padre1) - 2)
    hijo = padre1[:split] + [nodo for nodo in padre2 if nodo not in padre1[:split]]
   
    if hijo[0] != nodo_inicio:
        hijo.insert(0, nodo_inicio)
    if hijo[-1] != nodo_final:
        hijo.append(nodo_final)
    return hijo

def mutate(path):
    if len(path) > 2:
        i, j = random.sample(range(1, len(path) - 1), 2)
        path[i], path[j] = path[j], path[i]
    return path


poblacion = [random_path(grafo, nodos, nodo_inicio, nodo_final) for _ in range(tam_poblacion)]

for generacion in range(generaciones):
    poblacion = sorted(poblacion, key=fitness)
    nueva_poblacion = poblacion[:2]  

    while len(nueva_poblacion) < tam_poblacion:
        padres = random.sample(poblacion[:5], 2)  
        hijo = crossover(padres[0], padres[1])
        if random.random() < 0.1:  
            hijo = mutate(hijo)
        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

mejor_path = min(poblacion, key=fitness)

if fitness(mejor_path) == float('inf'):
    print("No se encontró un camino válido.")
else:
    print("Mejor camino:", mejor_path)
    print("Peso Total de la distancia final:", 1 / fitness(mejor_path))
