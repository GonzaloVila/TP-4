from linked_min_heap import LinkedMinHeap

def crear_min_heap():
    
    heap = LinkedMinHeap()

    print("Insertando elementos en el heap:")
    heap.insert(10)
    heap.insert(5)
    heap.insert(15)
    heap.insert(3)
    heap.insert(8)

    print("El minimo actual es:", heap.devolver_min())  #  3

    print("Extrayendo el minimo:", heap.sacar_min())  #  3
    print("El nuevo minimo es:", heap.devolver_min())  #  5

    print("Insertando 2 en el heap")
    heap.insert(2)

    print("El minimo actual es:", heap.devolver_min())  #  2

    print(f"Heap está vacio? {heap.is_empty()}") 
    while not heap.is_empty():
        print("Extrayendo:", heap.sacar_min())
    print(f"Heap esta vacio despues de extraer todos los elementos? {heap.is_empty()}")

if __name__ == "__main__":
    crear_min_heap()