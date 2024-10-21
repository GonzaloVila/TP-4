from typing import Any, List
from data_structures import BinaryTreeNode
from linkedbinarytreeExt import LinkedBinaryTreeExt

nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
nodo_c = BinaryTreeNode('C')
nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
nodo_g = BinaryTreeNode('G')
nodo_h = BinaryTreeNode('H')
nodo_i = BinaryTreeNode('I')
nodo_k = BinaryTreeNode('K')
nodo_m = BinaryTreeNode('M')
nodo_n = BinaryTreeNode('N')

arbol = LinkedBinaryTreeExt()

arbol.add_root(nodo_a)               
arbol.add_left_child(nodo_a, nodo_b)  
arbol.add_right_child(nodo_a, nodo_f) 
arbol.add_left_child(nodo_b, nodo_c)  
arbol.add_right_child(nodo_b, nodo_d) 
arbol.add_left_child(nodo_f, nodo_g)  
arbol.add_right_child(nodo_f, nodo_k) 
arbol.add_left_child(nodo_g, nodo_h)  
arbol.add_right_child(nodo_g, nodo_i) 
arbol.add_left_child(nodo_k, nodo_m)  
arbol.add_right_child(nodo_k, nodo_n) 

print("Arbol binario :")
print(arbol)

print("\nAncestro comun mas cercano entre H e I:")
ancestro = arbol.ancestro_mas_inmediato(nodo_h, nodo_i)
print(ancestro)

print("\nHojas del arbol:")
hojas = arbol.hojas()
print(hojas)

print("\nNivel del nodo M:")
nivel_m = arbol.nivel(nodo_m)
print(nivel_m)

print("\nDiametro del arbol (Camino mas largo entre 2 nodos):")
diametro_arbol = arbol.diametro()
print(diametro_arbol)

print("\n¿El arbol esta balanceado?")
balanceado = arbol.es_balanceado()
print(balanceado)