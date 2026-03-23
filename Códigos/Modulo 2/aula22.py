"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


import os


def soma(x,y,z):
    #Definição 
    print(f'{x=} {y=} {z=}','|','x + y + z = ', x+ y + z)
    
soma(1,2,3)
soma(y=2,z=3,x=1)

#Não recomendada, pois pode causar confusão
soma(1,2,z=5) #Argumento não nomeado (1,2) e argumento nomeado (z=5)

soma(1,y=2,z=34) 
#Apartir do momento que um argumento nomeado é usado, 
#os próximos argumentos devem ser nomeados também



print(1,2,3, sep='-') #sep é um argumento nomeado