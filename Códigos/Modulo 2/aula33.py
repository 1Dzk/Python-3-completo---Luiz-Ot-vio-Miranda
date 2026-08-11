# Métodos úteis dos dicionários do Python
# len - quantidade de chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com as chaves e valores
# get - obtem uma chave
# setdefault - define o valor de uma chave se ela não existir
# pop - remove e retorna o valor de uma chave (del)
# popitem - remove o último item adicionado
# update - atualiza o dicionário com outro dicionário ou pares chave-valor

pessoa = {
    "nome": "Henrique", 
    "sobrenome": "Pereira",
    "idade": 900,
    }

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
#print(len(pessoa)) 
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))
