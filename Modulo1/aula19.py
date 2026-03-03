"""
Exercício Gerar 2 número de um CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGÍTO,
    multiplicados por uma contagem regressiva começando de 11 e terminando em 2
    
Somar todos os resultados:
    Multiplicar o resultado por 10 e pegar o resto da divisão por 11


"""
import re
import sys

# cpf_enviado_usuario = '746.824.890-70'

entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
     '',
     entrada)


entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()


nove_digitos = cpf_enviado_usuario[:9] 
contagem_regressiva_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contagem_regressiva_1
    contagem_regressiva_1 -= 1
    
digito_1 = (resultado_digito_1 * 10 ) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
contagem_regressiva_2 = 11
resultado_digito_2 = 0 

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contagem_regressiva_2
    contagem_regressiva_2 -= 1
digito_2 = (resultado_digito_2 * 10 ) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'CPF Válido: {cpf_enviado_usuario}')
else:
    print(f'CPF Inválido')
