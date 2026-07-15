def classificacao(resultado):
    if resultado < 16.9:
        print ('Muito baixo do peso')
    elif resultado < 18.5:
        print ('Abaixo do peso')
    elif resultado < 25:
        print ('Peso normal')
    elif resultado < 30:
        print ('Acima do peso')
    elif resultado < 35:
        print ('Obesidade grau 1')
    elif resultado < 40:
        print ('Obesidade grau 2')
    else:
        print ('Obesidade grau 3')

def imc (kg, m):
    i = kg/(m*m)
    return i      

kg = float(input('Digite seu peso: '))
m = float(input('Digite sua altura: '))
imc = imc(kg, m)

print (f'O resultado do seu IMC eh: {imc}')
print (f'Voce esta classificado como:', end=' '); classificacao(imc)
