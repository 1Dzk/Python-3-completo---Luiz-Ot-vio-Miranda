""" Calculadora com while """


while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = None
    except:
        numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos os números são inválidos.')
            continue
        
        operadores_validos = '+-/*'
        
        if operador not in operadores_validos:
            print('Operador errado, tente novamente.')
            continue
        
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta.Confira seu resultado:')
    if operador == '+':
        print(f'{num1_float} + {num2_float} = ' ,num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = ' ,num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = ' ,num1_float / num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = ' ,num1_float * num2_float)
    else:
        print('Algo inesperado aconteceu.')
        
        
    
    sair = input('Deseja sair da calculadora? [s]im: ').lower().strip().endswith('s')
      

    if sair is True:
     print('Saindo da calculadora...')
     break