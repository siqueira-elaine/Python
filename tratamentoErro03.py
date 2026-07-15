def adicionar():
    try:
        x = float(input('Digite um número: '))
        y = float(input('Digite outro número: '))
        op = input('Digite a operação: (+, -, *, /): ')       

        match op:
            case '+':
                resultado = x + y
            case '-':
                resultado = x - y
            case '*':
                resultado = x * y
            case '/':
                resultado = x/y
            case _:
                raise ValueError('Operação inválida')
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
    except ValueError as e:
        if str(e) == 'Operação inválida':
            print('Operação inválida.')
        else:
            print('Digite somente números válidos.')
    else:
        print(f'O resultado deu {resultado}')
    finally:
        print('Caso Encerrado!')
adicionar()


# def adicionar():
#     try:
#         x = float(input('Digite um número: '))
#         y = float(input('Digite outro número: '))

#     except ValueError:
#         print('Digite somente números válidos.')

#     else:
#         op = input('Digite a operação (+, -, *, /): ')

#         try:
#             match op:
#                 case '+':
#                     resultado = x + y
#                 case '-':
#                     resultado = x - y
#                 case '*':
#                     resultado = x * y
#                 case '/':
#                     resultado = x / y
#                 case _:
#                     raise ValueError

#             print(f'O resultado deu {resultado}')
#         except ZeroDivisionError:
#             print('Não existe divisão por zero.')
    
#         except ValueError:
#             print('Operação inválida.')

#     finally:
#         print('Cálculo encerrado')

# adicionar()

# class MinhaExcecao(Exception):
#     pass

# try:
#     raise MinhaExcecao("Algo deu errado!")
# except MinhaExcecao as erro:
#     print(f"Erro capturado: {erro}")