import pandas as pd

cargos = []
salarios = []
qtd = int(input(f'Quantos cargos deseja cadastrar? '))

for i in range (qtd):
    print(f'Cadasro {i+1}: ')
    cargos.append(input('Digite o título do cargo: '))
    salarios.append(input('Digite o salário do cargo: '))

dados = {'cargos':cargos, 'salarios': salarios}
dados_inf = pd.DataFrame(dados)
print(dados_inf)