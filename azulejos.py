print('Hello World!')
import math

larg = float(input())
comp = float(input())
alt = float(input())

area = (larg*alt + comp*alt)*2

qtdcaixas = math.ceil(area/1.5)

print(f'A quantidade de caixas necessarias eh {qtdcaixas}')