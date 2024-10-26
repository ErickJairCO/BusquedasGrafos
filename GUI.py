import tkinter as tk
from tkinter import ttk
import GrafoNormal
import GrafoBPM
import GrafoBEMP


def ejecutar_busqueda():
    nodo_inicio = entry_inicio.get()
    nodo_fin = entry_fin.get()
    algoritmo = algoritmo_seleccionado.get()
    sentido = sentido_seleccionado.get()

    if algoritmo == 'BusquedaAncho':
        grafo = GrafoNormal.Grafo()
        grafo.leer_lista()  # Lectura de la lista de adyacencia
        ruta = grafo.ejecutar_bfs(nodo_inicio, nodo_fin)
    elif algoritmo == 'BusquedaProfundidad':
        grafo = GrafoNormal.Grafo()
        grafo.leer_lista()  # Lectura de la lista de adyacencia
        ruta = grafo.ejecutar_dfs(nodo_inicio, nodo_fin)
    elif algoritmo == 'BusquedaEMP':
        grafo = GrafoBEMP.Grafo
        grafo.construir_grafo()
        ruta = grafo.escalada_maxima_pendiente(nodo_inicio, nodo_fin, sentido == "Horario")
    elif algoritmo == "BusquedaPM":
        grafo_bpm = GrafoBPM.Grafo()
        grafo_bpm.leer_lista()
        grafo_bpm.leer_pesos()
        ruta = grafo_bpm.buscar_ruta_mejor_primero(nodo_inicio, nodo_fin, sentido.lower())
    else:
        ruta = "Algoritmo no seleccionado"

    resultado_label.config(text=f"Ruta: {ruta}")


ventana = tk.Tk()
ventana.title("Interfaz de Búsqueda")

# Campos de entrada de nodo inicial y final
tk.Label(ventana, text="Nodo Inicio:").grid(row=0, column=0)
entry_inicio = tk.Entry(ventana)
entry_inicio.grid(row=0, column=1)

tk.Label(ventana, text="Nodo Fin:").grid(row=1, column=0)
entry_fin = tk.Entry(ventana)
entry_fin.grid(row=1, column=1)

# Selección de algoritmo
tk.Label(ventana, text="Selecciona Algoritmo:").grid(row=2, column=0)
algoritmo_seleccionado = ttk.Combobox(ventana,
                                      values=["BusquedaAncho", "BusquedaProfundidad", "BusquedaEMP", "BusquedaPM"])
algoritmo_seleccionado.grid(row=2, column=1)

# Selección de sentido (Horario o Antihorario)
tk.Label(ventana, text="Selecciona Sentido:").grid(row=3, column=0)
sentido_seleccionado = ttk.Combobox(ventana, values=["Horario", "Antihorario"])
sentido_seleccionado.grid(row=3, column=1)

# Botón para ejecutar la búsqueda
ejecutar_btn = tk.Button(ventana, text="Ejecutar", command=ejecutar_busqueda)
ejecutar_btn.grid(row=4, column=0, columnspan=2)

# Label para mostrar el resultado
resultado_label = tk.Label(ventana, text="Ruta: ")
resultado_label.grid(row=5, column=0, columnspan=2)

print("Ejecutando interfaz gráfica")
ventana.mainloop()
