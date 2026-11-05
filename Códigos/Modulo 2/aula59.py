# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('ERRO: Divisão por zero')
except IndexError as error:
    print('ERRO: Índice inválido')
except (NameError, TypeError):
    print('ERRO: Nome ou Tipo inválido')
else :
   print('Não houve erro')
finally:
    print('FECHAR ARQUIVO')