def executa(funcao, *args):
    return funcao(*args)


def soma(a, b):
    return a + b

#def cria_multiplicador(multiplicador):
 #   def multiplicar(numero):
 #       return numero * multiplicador
   # return multiplicar

#duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))


print(
    executa(
        lambda a,b: a + b,
        2,3
    )
)


print(
    executa(
        lambda * args: sum(args),
        1,2,3,4,5,6,7
    )
)