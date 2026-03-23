""" 

Valores padrão para parametros
ao definir uma função, os parametros podem
ter valores padrão. Caso o valor não seja
enviado para o parametro, o valor padrão será
utilizado.
"""

def soma(x ,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1,2)
soma(5,2)
soma(20,32)
soma(y=9,z=0,x=1)