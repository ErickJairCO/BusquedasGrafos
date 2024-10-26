import csv
from collections import deque

class Grafo:

    def __init__(self):
        self.list_ady = {}

    def leer_lista(self):
        with open('lista_adyacencia.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 0:
                    nodo = row[0]
                    self.add_node(nodo)
                    for vecinos in row[1:]:
                        if vecinos.strip():
                            self.add_arista(nodo, vecinos)

    def add_node(self, node):
        if node not in self.list_ady:
            self.list_ady[node] = []

    def add_arista(self, node1, node2):
        self.list_ady[node1].append(node2)

    def dfs(self, inicio, final, sentido="horario", visitados=None, ruta=None):
        if visitados is None:
            visitados = set()
        if ruta is None:
            ruta = []

        visitados.add(inicio)
        ruta.append(inicio)

        if inicio == final:
            return ruta

        sucesores = self.list_ady.get(inicio, [])
        if sentido == "antihorario":
            sucesores = list(reversed(sucesores))

        for vecino in sucesores:
            if vecino not in visitados:
                resultado = self.dfs(vecino, final, sentido, visitados, ruta)
                if resultado:
                    return resultado

        ruta.pop()
        return None

    def bfs(self, inicio, final, sentido="horario"):
        visitados = set()
        cola = deque([[inicio]])

        while cola:
            ruta = cola.popleft()
            nodo_actual = ruta[-1]

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                if nodo_actual == final:
                    return ruta

                sucesores = self.list_ady.get(nodo_actual, [])
                if sentido == "antihorario":
                    sucesores = list(reversed(sucesores))

                for vecino in sucesores:
                    if vecino not in visitados:
                        nueva_ruta = list(ruta)
                        nueva_ruta.append(vecino)
                        cola.append(nueva_ruta)

        return None

    def ejecutar_dfs(self, inicio, final, sentido="horario"):
        ruta = self.dfs(inicio, final, sentido)
        if ruta:
            return f"Ruta encontrada (DFS): {' -> '.join(ruta)}"
        else:
            return "No se encontró una ruta con DFS."

    def ejecutar_bfs(self, inicio, final, sentido="horario"):
        ruta = self.bfs(inicio, final, sentido)
        if ruta:
            return f"Ruta encontrada (BFS): {' -> '.join(ruta)}"
        else:
            return "No se encontró una ruta con BFS."
