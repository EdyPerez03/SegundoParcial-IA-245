import csv
import random

def cargar_datos(archivo):
    datos = []
    with open(archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:
            datos.append(fila)
    return datos

datos_iris = cargar_datos(r'ejercicio1\\Iris.csv')
caracteristicas = datos_iris[0]
registros = datos_iris[1:]

for i in range(len(registros)):
    for j in range(len(registros[i]) - 1):
        registros[i][j] = float(registros[i][j])

for j in range(len(registros[0]) - 1):
    min_val = min(fila[j] for fila in registros)
    max_val = max(fila[j] for fila in registros)
    for i in range(len(registros)):
        registros[i][j] = (registros[i][j] - min_val) / (max_val - min_val)

columna_etiquetas = len(registros[0]) - 1
etiquetas_distintas = list(set(fila[columna_etiquetas] for fila in registros))
num_etiquetas = len(etiquetas_distintas)

etiquetas_a_indice = {etiqueta: i for i, etiqueta in enumerate(etiquetas_distintas)}
codificacion_one_hot = [[0] * num_etiquetas for _ in range(len(registros))]

for i, fila in enumerate(registros):
    indice = etiquetas_a_indice[fila[columna_etiquetas]]
    codificacion_one_hot[i][indice] = 1

for i in range(len(registros)):
    registros[i] = registros[i][:columna_etiquetas] + codificacion_one_hot[i]

class RedNeuronal:
    def __init__(self, entrada_size, oculto_size, salida_size):
        self.pesos_entrada_oculto = [[random.random() for _ in range(oculto_size)] for _ in range(entrada_size)]
        self.biases_entrada_oculto = [random.random() for _ in range(oculto_size)]
        self.pesos_oculto_salida = [[random.random() for _ in range(salida_size)] for _ in range(oculto_size)]
        self.biases_oculto_salida = [random.random() for _ in range(salida_size)]

    def funcion_sigmoide(self, valor):
        return 1 / (1 + (2.71828 ** -valor))

    def propagacion_adelante(self, X):
        z1 = [sum(X[i] * self.pesos_entrada_oculto[i][j] for i in range(len(X))) + self.biases_entrada_oculto[j] for j in range(len(self.biases_entrada_oculto))]
        a1 = [self.funcion_sigmoide(z) for z in z1]
        z2 = [sum(a1[i] * self.pesos_oculto_salida[i][j] for i in range(len(a1))) + self.biases_oculto_salida[j] for j in range(len(self.biases_oculto_salida))]
        a2 = [self.funcion_sigmoide(z) for z in z2]
        return a1, a2

    def retropropagacion(self, X, y, tasa_aprendizaje):
        a1, a2 = self.propagacion_adelante(X)
        error = [a2[i] - y[i] for i in range(len(y))]
        d_a2 = [error[i] * a2[i] * (1 - a2[i]) for i in range(len(a2))]

        dw2 = [[d_a2[j] * a1[i] for j in range(len(d_a2))] for i in range(len(a1))]
        db2 = d_a2

        d_a1 = [0] * len(a1)
        for i in range(len(a1)):
            d_a1[i] = sum(d_a2[j] * self.pesos_oculto_salida[i][j] for j in range(len(d_a2)))
        d_a1 = [d_a1[i] * a1[i] * (1 - a1[i]) for i in range(len(d_a1))]

        dw1 = [[X[j] * d_a1[i] for j in range(len(X))] for i in range(len(d_a1))]
        db1 = d_a1

        for i in range(len(self.pesos_oculto_salida)):
            for j in range(len(self.pesos_oculto_salida[i])):
                self.pesos_oculto_salida[i][j] -= tasa_aprendizaje * dw2[i][j]
        for i in range(len(self.biases_oculto_salida)):
            self.biases_oculto_salida[i] -= tasa_aprendizaje * db2[i]
        for i in range(len(self.pesos_entrada_oculto)):
            for j in range(len(self.pesos_entrada_oculto[i])):
                self.pesos_entrada_oculto[i][j] -= tasa_aprendizaje * dw1[i][j]
        for i in range(len(self.biases_entrada_oculto)):
            self.biases_entrada_oculto[i] -= tasa_aprendizaje * db1[i]

    def entrenar(self, X, y, tasa_aprendizaje, epocas):
        print("Objetivo: Clasificar correctamente las muestras en sus categorías correspondientes.")
        for epoca in range(epocas):
            for i in range(len(X)):
                self.retropropagacion(X[i], y[i], tasa_aprendizaje)

            if epoca % 100 == 0:
                _, salida = self.propagacion_adelante(X[0])
                error = sum((salida[j] - y[0][j]) ** 2 for j in range(len(y[0]))) / len(y[0])
                print(f'Época {epoca}, Error: {error}')

    def evaluar(self, X, y, etiquetas_unicas):
        print("\nResultados:")
        correctas = 0
        for i in range(len(X)):
            _, salida = self.propagacion_adelante(X[i])
            prediccion = etiquetas_unicas[salida.index(max(salida))]
            real = etiquetas_unicas[y[i].index(1)]
            print(f"Entrada: {X[i]} -> Predicción: {prediccion}, Real: {real}")
            if prediccion == real:
                correctas += 1
        precision = correctas / len(X) * 100
        print(f"\nPrecisión: {precision:.2f}%")
        if precision >= 90:
            print("¡Salida buena! El modelo clasifica correctamente la mayoría de los datos.")
        else:
            print("Salida mala. El modelo necesita mejorar.")


tamaño_entrada = len(registros[0]) - num_etiquetas
tamaño_oculto = 5
tamaño_salida = num_etiquetas
tasa_aprendizaje = 0.4
epocas = 1000

X = [fila[:tamaño_entrada] for fila in registros]
y = [fila[tamaño_entrada:] for fila in registros]

red_neuronal = RedNeuronal(tamaño_entrada, tamaño_oculto, tamaño_salida)
red_neuronal.entrenar(X, y, tasa_aprendizaje, epocas)

etiquetas_unicas_ordenadas = [k for k, v in sorted(etiquetas_a_indice.items(), key=lambda item: item[1])]
red_neuronal.evaluar(X, y, etiquetas_unicas_ordenadas)
