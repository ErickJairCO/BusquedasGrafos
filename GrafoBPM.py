import csv

class Grafo:
    def __init__(self):
        self.list_ady = {}
        self.pesos = {}  # Diccionario para almacenar la matriz de pesos
        self.valores_heuristicos = {}

    def leer_lista(self):
        with open('lista_adyacencia.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 0:
                    nodo = row[0]
                    self.add_node(nodo)
                    for vecino in row[1:]:
                        if vecino.strip():  # Ignora celdas vacías
                            self.add_arista(nodo, vecino)

    def leer_pesos(self):
        with open('TablaGrafo.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Nombres de nodos como cabecera
            for row in reader:
                nodo_origen = row[0]
                for i, peso in enumerate(row[1:], start=1):
                    if peso.strip():  # Ignora celdas vacías
                        nodo_destino = headers[i]
                        self.pesos[(nodo_origen, nodo_destino)] = int(peso)

    def add_node(self, node):
        if node not in self.list_ady:
            self.list_ady[node] = []

    def add_arista(self, node1, node2):
        if node1 in self.list_ady:
            self.list_ady[node1].append(node2)

    def obtener_valor_arco(self, nodo1, nodo2):
        peso = self.pesos.get((nodo1, nodo2))
        if peso is None:
            peso = self.pesos.get((nodo2, nodo1))
        return peso if peso is not None else float('inf')

    def obtener_valor_heuristico(self, nodo_act, nodo_final):
        return self.pesos.get((nodo_act, nodo_final), float('inf'))

    def buscar_ruta_mejor_primero(self, nodo_inicial, nodo_final, sentido="horario"):
        cola_prioridad = [(0, nodo_inicial, [nodo_inicial])]
        visitados = set()

        while cola_prioridad:
            cola_prioridad.sort(key=lambda x: x[0])
            f_actual, nodo_act, ruta = cola_prioridad.pop(0)

            if nodo_act == nodo_final:
                return ruta

            if nodo_act in visitados:
                continue
            visitados.add(nodo_act)

            sucesores = self.list_ady.get(nodo_act, [])
            if sentido == "antihorario":
                sucesores = list(reversed(sucesores))

            for sucesor in sucesores:
                if sucesor not in visitados:
                    g = f_actual + self.obtener_valor_arco(nodo_act, sucesor)
                    h = self.obtener_valor_heuristico(sucesor, nodo_final)
                    f = g + h
                    nueva_ruta = ruta + [sucesor]
                    cola_prioridad.append((f, sucesor, nueva_ruta))

        return None
