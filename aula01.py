import pandas

dataFrame = pandas.read_csv('csv/ex03.csv', sep=";")

print('Total de entregas: ', dataFrame["Entregas"].sum())
print('Media das avaliações: ', dataFrame["Avaliação"].mean())
print('Entregador com mais entregas: ', dataFrame["Entregador"] where dataFrame["Entregas"].max())
print('Entregador com menos entregas: ', dataFrame["Entregador"] where dataFrame["Entregas"].min())
print('Entregador com avaliação maior que 4.6: ', dataFrame["Avaliação"] > 4.6)

""" import pandas

dataFrame = pandas.read_csv('csv/ex03.csv', sep=";")

print('Total de entregas:', dataFrame["Entregas"].sum())
print('Media das avaliações:', dataFrame["Avaliação"].mean())

print(
    'Entregador com mais entregas:',
    dataFrame.loc[dataFrame["Entregas"].idxmax(), "Entregador"]
)

print(
    'Entregador com menos entregas:',
    dataFrame.loc[dataFrame["Entregas"].idxmin(), "Entregador"]
)

print(
    'Entregadores com avaliação maior que 4.6:\n',
    dataFrame.loc[dataFrame["Avaliação"] > 4.6, "Entregador"]
)

Se você estiver aprendendo pandas agora, vale lembrar que não existe a sintaxe SQL WHERE dentro do Python. 
Em pandas, os filtros são feitos com expressões como:

dataFrame[dataFrame["Avaliação"] > 4.6]

ou

dataFrame.loc[dataFrame["Avaliação"] > 4.6] """