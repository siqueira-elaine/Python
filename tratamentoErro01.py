def divisao(dividendo,divisor):
    try: 
        resultado = dividendo/divisor
    except ZeroDivisionError:
        print('Não seja burro, não existe divisão por zero.')
    else:
        print(f'{resultado}')
    finally:
        print('Finish!')

try:
    dividendo  = int(input('Dividendo: '))
    divisor  = int(input('Divisor: '))
    divisao(dividendo, divisor)
except ValueError:
        print('Presta atenção, dgita o número direito.')
