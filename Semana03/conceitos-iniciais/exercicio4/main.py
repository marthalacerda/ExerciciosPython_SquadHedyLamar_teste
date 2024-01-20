# 4. Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.

litros = float(input('Informe a quantidade de litros:\n'))
distancia = float(input('Informe a distância percorrida em km:\n'))


print('Consumo médio em km/l é de :', float("{:.2f}".format(distancia / litros)))