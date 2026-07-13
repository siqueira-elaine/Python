import pandas
import numpy as np

ARQUIVO = 'CSV/01.amazon_sales_dataset.csv'

try:
    df = pandas.read_csv(ARQUIVO)
    total_vendas = np.array(df['total_sales'])
    print('Media: ', np.mean(total_vendas))
    print('Mediana: ', np.median(total_vendas))
    print('Diferença entre media e mediana (%): ', np.mean(total_vendas)/np.median(total_vendas))
    
except Exception as e:
    print(f'Erro: {e}')