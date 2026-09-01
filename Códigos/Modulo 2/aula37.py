# Sets - Conjuntos em Python (tipo set)
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1,2,3}

#s1 = set('Luiz')
#s1 = set() #vazio
#s1 = {'Luiz',1,2,3} #com dados


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores duplicados;
# - Seus valores sempre serão únicos;
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
#l1 = [1,2,3,3,3,3,7,8,9]
#s1 = set(l1)
#l2 = list(s1)
#print(l2) 

s1 = {1,2,3,4,5}
print(s1)


# Métodos úteis:
# add, update, clear, discard
