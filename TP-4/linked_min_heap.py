from typing import Any, Optional
from src.python_ed_fcad_uner.data_structures.linear.list_node import ListNode
from src.python_ed_fcad_uner.data_structures.linear.lists.linked_list import LinkedList

class LinkedMinHeap:
    
    def __init__(self) -> None:
        self._heap = LinkedList()

    def is_empty(self) -> bool:
        return self._heap.is_empty()

    def insert(self, element: Any) -> None:
        self._heap.append(element)
        self.ajusta_up()

    def sacar_min(self) -> Optional[Any]:
        if self.is_empty():
            return None
        
        min_element = self._heap[0] 
        last_element = self._heap[len(self._heap) - 1]
        self._heap[0] = last_element
        del self._heap[len(self._heap) - 1]  
        
        self.ajusta_down()

        return min_element

    def ajusta_up(self) -> None:
        index = len(self._heap) - 1 
        while index > 0:
            parent_index = (index - 1) // 2  
            if self._heap[index] < self._heap[parent_index]:
                self.cambiar(index, parent_index)
                index = parent_index
            else:
                break  #lugar correcto

    def ajusta_down(self) -> None:
        index = 0 #rsiz
        while 2 * index + 1 < len(self._heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smaller_child_index = left_child_index

            if right_child_index < len(self._heap) and self._heap[right_child_index] < self._heap[left_child_index]:
                smaller_child_index = right_child_index

            if self._heap[index] > self._heap[smaller_child_index]:
                self.cambiar(index, smaller_child_index)
                index = smaller_child_index
            else:
                break  # lugar correvto

    def cambiar(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def devolver_min(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._heap[0]