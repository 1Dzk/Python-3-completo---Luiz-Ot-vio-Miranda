"""
CRUD - Create, Read, Update, Delete
ja esta sendo utilizado em list[]
"""

#Read
list =[1,2,3,4]
print(list[2])

#Update
list[2] = 10
print(list[2])

#Delete
del list[2]
print(list)
print(list[2])

#Insert
list.append(320) #adiciona um elemento no final da lista
list.append(323220) #adiciona um elemento no final da lista
list.pop() #remove o ultimo elemento da lista
print(list)