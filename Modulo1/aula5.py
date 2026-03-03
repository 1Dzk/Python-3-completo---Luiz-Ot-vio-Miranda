"""
Concatenar listas em Python

extend - adiciona os elementos de uma lista a outra lista

"""


list1 = [1,2,3]
list2 = [4,5,6]
lista3 = list1 + list2
list1.extend(list2) #extend nao retorna nada, ele modifica a lista1
print(list1)