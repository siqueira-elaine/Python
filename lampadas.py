print('Hello World!')

potlamp = int(input())
larg = float(input())
comp = float(input())
mq = larg*comp

bocais = mq/3
potnec = 3*mq

qtdlamp = potnec/potlamp

if qtdlamp <= bocais:
    print(f'A quantidade de lampadas necessarias eh {qtdlamp}')
else:  
    print(f'A quantidade de lampadas necessarias ({qtdlamp}) eh maior que a quantidade de bocais disponiveis ({bocais})')
    print(f'Para essa quantidade de bocais, aumente a potencia das suas lampadas para pelo menos {int(potnec/bocais)} watts')
