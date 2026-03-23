"""
Exercício Gerar 1 número de um CPF
    CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF 
multiplicados por uma contagem regressiva começando de 10 e terminando em 1

Somar todos os resultados:
Multiplicar o resultado por 10 e pegar o resto da divisão por 11

Se o resultado for maior que 9, o dígito é 0, caso contrário, o dígito é o resultado da conta
"""

cpf = '74682489070'
nove_digitos = cpf[:9]
contagem_regressiva_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contagem_regressiva_1
    contagem_regressiva_1 -= 1
    
digito_1 = (resultado_digito_1 * 10 ) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
    

