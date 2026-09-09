# Função em lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista=[
#       {'nome ' : 'Luiz' , · 'sobrenome ' : · 'miranda' },
#       {'nome ' : · 'Maria', · 'sobrenome ' : · 'Oliveira' },
#       {'nome ' : · 'Danie1 ' , · 'sobrenome ' : · 'Silva' },
#       { 'nome ' : 'Eduardo' , · ' sobrenome ' : · 'Moreira' },
#       {'nome' : 'Aline', . 'sobrenome ' : 'Souza' },
# ]

# lista = [1,2,5,63,55,12,6,10,22]
# lista.sort() # ordena
# lista.sort(reverse=True) # inverte
# sorted(lista)

lista = [
    {"nome": "Luiz", "sobrenome": "miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel ", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item["nome"]) 
l2 = sorted(lista, key=lambda item: item["sobrenome"]) 

exibir(l1)
exibir(l2)