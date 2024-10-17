import csv

#implementacion para la creacion de grafos

class Grafo():
    
    #constructor de inicializacion del grafo
    def __init__(self):
        self.list_ady = {}

    def leer_lista(self, ruta_archivo):
        with open(ruta_archivo, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                #print(row)  # imprime cada fila como una lista
                if len(row) > 0:
                    nodo = row[0]
                    self.add_node(nodo)
                    #Agregamos sus aristas
                    for vecinos in row[1:]:
                        self.add_arista(nodo,vecinos)


    def add_node(self, node):
        self.list_ady[node] = []
    
    def add_arista(self, node1, node2):
        self.list_ady[node1].append(node2)
        #self.list_ady[node2].append(node1)
    
    def print_list_ady(self):
        for node, vecinos in self.list_ady.items():
            print(f"{node} -> {vecinos}")

g = Grafo()
g.leer_lista("ruta")
g.print_list_ady()
    