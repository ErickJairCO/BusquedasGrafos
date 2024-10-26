import tkinter as tk
from tkinter import ttk

#import GrafoBPM
import GrafoNormal
import GrafoBPM

def ejecutar_busqueda():
    nodo_inicio = entry_inicio.get()
    nodo_fin = entry_fin.get()
    algoritmo = algoritmo_seleccionado.get()

    if algoritmo in ['BusquedaAncho', 'BusquedaProfundidad']:
        print('seleccion1')
        ruta = GrafoNormal.Grafo.ejecutar_busqueda()
    elif algoritmo == 'BusquedaEMP':
        print('seleccion2')
        #ruta = GrafoBEMP.escalada_maxima_pendiente()
    elif algoritmo == "BusquedaPM":
        print('seleccion3')
        grafo_bpm = GrafoBPM.Grafo()
        ruta =  grafo_bpm.buscar_ruta_mejor_primero(nodo_inicio, nodo_fin)
    else:
        ruta = "Algoritmo no seleccionado"

    resultado_label.config(text=f"Ruta: {ruta}")

ventana = tk.Tk()
ventana.title("Interfaz de Búsqueda")

tk.Label(ventana, text="Nodo Inicio:").grid(row=0, column=0)
entry_inicio = tk.Entry(ventana)
entry_inicio.grid(row=0, column=1)

tk.Label(ventana, text="Nodo Fin:").grid(row=1, column=0)
entry_fin = tk.Entry(ventana)
entry_fin.grid(row=1, column=1)

tk.Label(ventana, text="Selecciona Algoritmo:").grid(row=2, column=0)
algoritmo_seleccionado = ttk.Combobox(ventana, values=["BusquedaAncho", "BusquedaProfundidad", "BusquedaEMP", "BusquedaPM"])
algoritmo_seleccionado.grid(row=2, column=1)

ejecutar_btn = tk.Button(ventana, text="Ejecutar", command=ejecutar_busqueda)
ejecutar_btn.grid(row=3, column=0, columnspan=2)

resultado_label = tk.Label(ventana, text="Ruta: ")
resultado_label.grid(row=4, column=0, columnspan=2)

print("Ejecutando interfaz gráfica")
ventana.mainloop()
