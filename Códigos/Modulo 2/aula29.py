"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saldar(nome):
        return f'{saudacao}, {nome}!'
    return saldar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Henrique', 'Maria', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
