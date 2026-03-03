"""
split e join com list e str 
split - divide uma string 
join - junta uma lista em uma string

"""
frase = 'O Cruzeiro é muito ruim meu Deus, socorro'

lista_palavras = frase.split(', ')

for i,frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())
    
print(lista_palavras)