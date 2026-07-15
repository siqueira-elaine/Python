import pandas

print(pandas.read_excel('bancos.xlsx')['Banco'])

# tail() : p/ exibir últimos registros;
# head() : p/ exibir primeiros registros
# array[nome_da_coluna] : p/ especificar a(s) coluna(s) a ser(em) exibida(s) 
# array[array[nome_da_coluna] operador_lógico valor_da_coluna] : p/ filtrar pelo valor dos registros desejados em determinada coluna
# read_csv('nome_do_arquivo.csv') : le dados e um arquivo csv
# to_csv : salva o dataframe em um arqivo csv 