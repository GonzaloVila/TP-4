from typing import Any, Tuple
from sorted_priority_queue_abstract import SortedPriorityQueueAbstract 
from src.python_ed_fcad_uner.data_structures.priority_queues.priority_queue_base import PriorityQueueBase

class SortedPriorityQueue(SortedPriorityQueueAbstract):
    def __init__(self) -> None:
        self._data = []  

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def add(self, k: Any, v: Any) -> None:
        new_item = PriorityQueueBase._Item(k, v)  
        self._data.append(new_item)  
        self._data.sort()  

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La cola de prioridad está vacía.")
        item = self._data[0]  
        return (item._key, item._value)

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La cola de prioridad está vacía.")
        item = self._data.pop(0)  
        return (item._key, item._value)

    def __str__(self) -> str:
        return ", ".join(str(item) for item in self._data)
