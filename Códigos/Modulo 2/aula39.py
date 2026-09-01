# Operadores úteis:
# union | união - Une
# intersection & (inserseção) - Itens presentes em ambos os sets
# difference -, - Itens presentes apenas no set da esquerda
# symmetric_difference ^ - Itens que não estão em ambos os sets

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
print(s3)
s3 = s2 - s1 
print(s3) # 4
s3 = s1 - s2 
print(s3) # 1
s3 = s1 ^ s2
print(s3)