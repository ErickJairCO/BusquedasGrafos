import csv


class Grafo():

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
                    # Añadimos sucesores sin peso
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
        """Obtiene el peso entre dos nodos, intentando ambos órdenes."""
        peso = self.pesos.get((nodo1, nodo2))
        if peso is None:
            peso = self.pesos.get((nodo2, nodo1))
        return peso if peso is not None else float('inf')

    def obtener_valor_heuristico(self, nodo_act, nodo_final):
        return self.pesos.get((nodo_act, nodo_final), float('inf'))

    def buscar_ruta_mejor_primero(self, nodo_inicial, nodo_final):
        # Cola de prioridad simulada como lista
        cola_prioridad = [(0, nodo_inicial, [nodo_inicial])]
        visitados = set()

        while cola_prioridad:
            # Ordenar la lista para que el primer elemento sea el de menor f
            cola_prioridad.sort(key=lambda x: x[0])
            f_actual, nodo_act, ruta = cola_prioridad.pop(0)

            print(f"Visitando nodo {nodo_act} con costo acumulado {f_actual}")

            if nodo_act == nodo_final:
                print(f"Ruta encontrada: {ruta} con costo total: {f_actual}")
                return ruta

            if nodo_act in visitados:
                continue
            visitados.add(nodo_act)

            for sucesor in self.list_ady.get(nodo_act, []):
                if sucesor not in visitados:
                    g = f_actual + self.obtener_valor_arco(nodo_act, sucesor)
                    h = self.obtener_valor_heuristico(sucesor, nodo_final)
                    f = g + h
                    nueva_ruta = ruta + [sucesor]

                    print(f"  Sucesor {sucesor} con g = {g}, h = {h}, f = {f}")

                    cola_prioridad.append((f, sucesor, nueva_ruta))

        print("Ruta no encontrada.")
        return None

'''
# Ejemplo de uso
grafo = Grafo()
grafo.leer_lista("lista_adyacencia.csv")
grafo.leer_pesos("TablaGrafo.csv")

# Realizar la búsqueda
grafo.buscar_ruta_mejor_primero('8', '14')'''

'''
grafo = Grafo()
grafo.leer_lista("lista_adyacencia.csv")
grafo.leer_pesos("TablaGrafo.csv")
#grafo.imprimir_pesos()

n = '11'
n2 = '1'
# Ejemplo de obtener peso entre nodos específicos
peso = grafo.obtener_peso(n, n2)
print(f"Peso entre nodo {n} y nodo {n2}: {peso}")

grafo.buscar_ruta_mejor_primero('8','18')'''