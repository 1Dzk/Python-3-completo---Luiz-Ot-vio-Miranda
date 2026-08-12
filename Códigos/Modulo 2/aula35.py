# Métodos úteis dos dicionários do Python - Parte 2
# len - quantidade de chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com as chaves e valores
# get - obtem uma chave
# setdefault - define o valor de uma chave se ela não existir
# pop - remove e retorna o valor de uma chave (del)
# popitem - remove o último item adicionado
# update - atualiza o dicionário com outro dicionário ou pares chave-valor

p1 = {
    "nome": "Henrique",
    "sobrenome": "Pereira",
}

# print(p1.get('nome'))
# print(p1.get('nome', 'Não existe')) # se não existir, retorna o valor padrão

#nome = p1.pop("nome")
# print(nome)
#print(p1)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

#p1.update({
  #  'nome': 'Novo valor',
 #   'idade': 18,
#})
#p1.update(nome= 'Novo valor', idade=19)
tupla = ('nome', 'Novo valor'),('idade', 19)
p1.update(tupla)
print(p1)