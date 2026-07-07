# Exercícios com funções 

# Crie uma funçãoque multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
        print("Total parcial:", total)
    return total

multiplicacao = multiplica(1,2,3,4,5)
print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return print(f'O número {numero} é par')
    else:
        return print(f'O número {numero} é impar')

par_ou_impar(5)
par_ou_impar(10)