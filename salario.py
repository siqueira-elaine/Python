def inss(salario):
    if salario >= 1800:
        inss = salario*0.11
        desconto = 11
    else: 
        inss = salario*0.09
        desconto = 9
    print (f'O desconto para o seu INSS eh de {desconto}% do seu salario bruto, que equivale a R$ {inss}.')
    return inss

def vale(salario):
    if salario >= 1500:
        vale = salario*0.06
        desconto = 6
    else: 
        vale = salario*0.05
        desconto = 5
    print (f'O desconto para o seu vale transporte eh de {desconto}% do seu salario bruto, que equivale a R$ {vale}.')
    return vale
    
def bonus(salario):
    if salario >= 1240:
        bonus = 700
    else: 
        bonus = 500
    print (f"Seu bonus eh R$ {bonus}")
    return bonus

def funcao(salario):
    if salario >= 3000:
        funcao = "Acionista"
    elif salario >= 2000:
        funcao = "Gerente"
    else: 
        funcao = "Vendedor"
    print (f"Sua funcao na carteira eh: {funcao}")
    return funcao

def liquido (nome, bruto):
    liquido = bruto-(inss(bruto)+vale(bruto))+bonus(bruto)
    print (f"{nome}, seu salario liquido eh R$ {liquido}")    

nome = str(input('\nDigite seu nome: '))
bruto = float(input('Digite seu salario bruto: '))

funcao (bruto)
liquido(nome, bruto)