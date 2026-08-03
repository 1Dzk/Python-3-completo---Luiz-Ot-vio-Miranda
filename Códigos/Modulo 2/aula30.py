#Exercícios
#Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

print(criar_multiplicador(2)(5))  # Duplicar 5
print(criar_multiplicador(3)(5))  # Triplicar 5  
print(criar_multiplicador(4)(5))  # Quadruplicar 5