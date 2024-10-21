from sorted_priority_queue import SortedPriorityQueue

def test_sorted_priority_queue():
    # Crear una instancia de SortedPriorityQueue
    spq = SortedPriorityQueue()

    # Prueba inicial: verificar que la cola esté vacía
    print(f"La cola está vacía? {spq.is_empty()}")

    print(f"Tamaño inicial de la cola: {len(spq)}\n") 

    # Agregar algunos elementos
    spq.add(4, "A")
    spq.add(3, "B")
    spq.add(8, "C")
    spq.add(1, "D")
    spq.add(0, "E")
    print("Se han agregado los elementos (4, 'A'), (3, 'B'), (8, 'C'), (1, 'D'), (0, 'E').")
    print(f"Tamaño después de las inserciones: {len(spq)}")
    print(f"Cola: {str(spq)}\n")

    # Llamo al método min() para saber cual es la menor clave
    min_item = spq.min()
    print(f"El item con la menor clave es: {min_item}\n")

    # Probar el método remove_min() para eliminar el ítem con menor clave
    removed_item = spq.remove_min()
    print(f"item de menor clave eliminado: {removed_item}")
    print(f"Tamaño después de eliminar el ítem con menor clave: {len(spq)}")
    print(f"Cola después de eliminar el item con la menor clave: {spq}\n")

    # Verificar que el nuevo elemento mínimo sea correcto
    min_item = spq.min()
    print(f"El nuevo ítem con menor clave es: {min_item}\n")

    # Eliminamos el resto de elementos de la cola para luego verificar si está vacía.
    spq.remove_min()  #aca elimina 1, D
    spq.remove_min()  #aca elimina 3, B
    spq.remove_min()  #aca elimina 4, A
    spq.remove_min()  #aca elimina 8, C
    print("Se eliminaron todos los elementos restantes para probar de nuevo el is_empty().")
    print(f"La cola está vacía? {spq.is_empty()}")
    print(f"Tamaño actual de la cola: {len(spq)}")
    print(f"Str: '{str(spq)}'")

if __name__ == "__main__":
    test_sorted_priority_queue()
