from Array_heap_ext import ArrayHeapExt

def crear_heap():
    # Crear el heap y agregar los elementos para que coincidan con el diagrama
    heap = ArrayHeapExt()
    
    heap.add(2, 'B')
    heap.add(5, 'A')
    heap.add(4, 'C')
    heap.add(15, 'K')
    heap.add(9, 'F')
    heap.add(7, 'Q')
    heap.add(6, 'Z')
    heap.add(16, 'X')
    heap.add(25, 'J')
    heap.add(14, 'E')
    heap.add(12, 'H')
    heap.add(11, 'S')
    heap.add(8, 'W')
    heap.add(20, 'B')
    heap.add(10, 'L')

    print("Heap después de agregar todos los elementos:")
    print(heap)

    return heap

def test_array_heap_ext():
    
    # Crea el heap pedido en la imagen
    heap = crear_heap()
    print("\n")

    # Probar min()
    print("Elemento con menor clave (min):", heap.min())
    print("\n")

    #  eliminar por prioridad 
    print("Eliminar nodo con clave 10:")
    heap.eliminar_por_prioridad(10)
    print(heap)
    print("\n")

    # cambiar prioridad 
    print("Cambiar la clave del nodo con clave 6 a 1:")
    heap.cambiar_prioridad(6, 1)
    print(heap)
    print("\n")

    # fusionar otro heap
    otro_heap = ArrayHeapExt()
    otro_heap.add(18, 'M')
    otro_heap.add(3, 'N')
    
    print("Fusionar con otro heap:")
    heap.fusionar(otro_heap)
    print(heap)
    print("\n")

    # vaciar el heap
    print("Vaciar heap:")
    heap.vaciar()
    print(heap)

if __name__ == "__main__":
    test_array_heap_ext()