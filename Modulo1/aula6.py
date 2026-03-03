"""
Cuidado com os mutáveis

= - copiando os valores (imutáveis)
= - aponta para o mesmo local na memória (mutáveis)

"""
#nome_outra_variavel = nome
#nome = 'João'
#print(nome)
#print(nome_outra_variavel)
# nome[1] = 'a' #string é imutável, nao pode ser alterada


list_a = ['Luiz', 'Henrique', 'Maria',1,2,2.2]
lista_b = list_a.copy()

list_a[0] = 'Aleatorio'

print(lista_b)
print(list_a)


