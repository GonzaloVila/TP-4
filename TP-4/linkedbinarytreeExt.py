from typing import Any, List, Tuple
from data_structures import BinaryTreeNode
from data_structures import LinkedBinaryTree
from linkedbinarytreeExtAbstract import LinkedBinaryTreeExtAbstract
from data_structures import LinkedQueue

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):
    def hojas(self) -> List[Any]:
        lista = []
        stack = [self._root]

        while stack:
            nodo = stack.pop()
            
            if nodo is not None and nodo.children_count == 0:
                lista.append(nodo.element)
            
            if nodo is not None:
                if nodo.right_child:
                    stack.append(nodo.right_child)
                if nodo.left_child:
                    stack.append(nodo.left_child)
        return lista

    def ancestro_mas_inmediato(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> BinaryTreeNode:
        camino_nodo1 = []
        actual = nodo1
        while actual:
            camino_nodo1.append(actual)
            actual = self._search_parent(actual)
        camino_nodo1.reverse()

        camino_nodo2 = []
        actual = nodo2
        while actual:
            camino_nodo2.append(actual)
            actual = self._search_parent(actual)
        camino_nodo2.reverse()
        
        ancestro_comun = None
        for ancestro1, ancestro2 in zip(camino_nodo1, camino_nodo2):
            if ancestro1 == ancestro2:
                ancestro_comun = ancestro1
            else:
                break
        
        return ancestro_comun
    
    def nivel(self, nodo: BinaryTreeNode) -> int:
        if self.is_empty():
            raise Exception("El arbol esta vacio.")
        
        queue = LinkedQueue()
        queue.enqueue(self._root)

        nivel_actual = 0

        while not queue.is_empty():
            size = len(queue)

            for _ in range(size):
                actual = queue.first()

                if actual == nodo: 
                    return nivel_actual

                if actual.left_child:
                    queue.enqueue(actual.left_child)
                if actual.right_child:
                    queue.enqueue(actual.right_child)

                queue.dequeue()

            nivel_actual += 1
    
    def diametro(self) -> int:
        if self.is_empty():
            return 0

        queue = LinkedQueue()
        queue.enqueue(self._root)
        max_width = 0

        while not queue.is_empty():
            size = len(queue)
            max_width = max(max_width, size)

            for _ in range(size):
                actual = queue.dequeue()
                if actual.left_child:
                    queue.enqueue(actual.left_child)
                if actual.right_child:
                    queue.enqueue(actual.right_child)

        return max_width

    def es_balanceado(self) -> bool:
        if self._root is None:
            return True 
        
        def verificar_balanceado(nodo: BinaryTreeNode) -> Tuple[bool, int]:
            if nodo is None:
                return True, 0
            
            balance_izq, altura_izq = verificar_balanceado(nodo.left_child)
            balance_der, altura_der = verificar_balanceado(nodo.right_child)

            balance_actual = balance_izq and balance_der and abs(altura_izq - altura_der) <= 1
            
            return balance_actual, max(altura_izq, altura_der) + 1

        balanceado, _ = verificar_balanceado(self._root)
        return balanceado