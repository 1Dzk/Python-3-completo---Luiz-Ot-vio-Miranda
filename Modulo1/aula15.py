"""
Listas de listas e seus indices

"""

salas = [

['Maria', 'João', 'Pedro'],

['Sofia',],

['Lucas', 'Ana', 'Carlos'],

]

# print(salas[0][0])
# print(salas[1][0])
# print(salas[2][3][2])

for sala in salas:
    print(f'Lista de alunos da sala: {sala}')
    for aluno in sala:
        print(aluno)
