# Lista de compras
import os

lista_compras = []

while True:
    print('Selecione uma opção:')
    print('1 - Listar itens')
    print('2 - Adicionar item')
    print('3 - Remover item')
    print('4 - Sair')

    input_usuario = input('Digite o número da opção desejada: ')
    
    if input_usuario == '1':
        os.system('cls')
        if len(lista_compras) == 0:
            print('A lista de compras está vazia.\n')
        else:
            print('Itens da lista:')
            for i, valor in enumerate(lista_compras, 1):
                print(f'{i} - {valor}')
            print()
    
    elif input_usuario == '2':
        os.system('cls')
        valor_lista = input('Digite o item a adicionar: ').strip()
        if valor_lista:
            lista_compras.append(valor_lista)
            print(f'Item "{valor_lista}" adicionado com sucesso!\n')
        else:
            print('Item não pode estar vazio!\n')
    
    elif input_usuario == '3':
        os.system('cls')
        valor_lista = input('Digite o item a remover: ').strip()
        if valor_lista in lista_compras:
            lista_compras.remove(valor_lista)
            print(f'Item "{valor_lista}" removido com sucesso!\n')
        else:
            print('Item não encontrado na lista.\n')
    
    elif input_usuario == '4':
        print('Saindo...')
        break
    
    else:
        print('Opção inválida!\n')