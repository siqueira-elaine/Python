import pandas as pd

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios': [1000, 2000, 3000, 4000]
}

dados_emp = pd.DataFrame(dados)
dados_emp.index = dados_emp.index + 1
print(dados_emp)