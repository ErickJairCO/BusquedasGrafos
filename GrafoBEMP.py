import csv

class Grafo:
    def __init__(self):
        self.grafo = {}  # Define self.grafo como un atributo de instancia

    # Lectura del archivo CSV y construcción del grafo
    def construir_grafo(self, archivo_csv='valores.csv'):
        with open(archivo_csv, mode='r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera si existe
            for fila in lector_csv:
                nodo_inicial = int(fila[0])
                if nodo_inicial not in self.grafo:
                    self.grafo[nodo_inicial] = []
                for i in range(1, len(fila[1:]), 2):
                    if fila[i] and fila[i + 1]:
                        valor = int(fila[i])
                        sucesor = int(fila[i + 1])
                        self.grafo[nodo_inicial].append((sucesor, valor))
        print("Grafo construido:", self.grafo)

    # Algoritmo de Escalada Máxima Pendiente
    def escalada_maxima_pendiente(self, inicio, fin, sentido_horario=True):
        ruta = [inicio]
        nodo_actual = inicio
        visitados = set()

        while nodo_actual != fin:
            if nodo_actual not in self.grafo or not self.grafo[nodo_actual]:
                print("No hay Ruta. Sin sucesores.")
                return None

            # Ordenar sucesores por peso y aplicar sentido de búsqueda
            vecinos = sorted(self.grafo[nodo_actual], key=lambda x: x[1], reverse=not sentido_horario)
            nodo_siguiente = None

            for vecino in vecinos:
                if vecino[0] not in visitados:
                    nodo_siguiente = vecino[0]
                    break

            if nodo_siguiente is None:
                print("No existe Ruta")
                return None

            ruta.append(nodo_siguiente)
            visitados.add(nodo_actual)
            nodo_actual = nodo_siguiente
            print("Nodo actual:", nodo_actual)

        return ruta
