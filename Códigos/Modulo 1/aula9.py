
"""
Desempacotamento de listas

"""
nome1 , nome2 , nome3 = ['Luiz','Henrique','Maria']

print(nome2)   


_ , _ , nome3,*resto = ['Luiz','Henrique','Maria']
print(nome3,resto)