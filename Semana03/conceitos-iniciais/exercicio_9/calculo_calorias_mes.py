# 9. Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.

horas_exercicios_semana = int(input("Quantas horas por semana você pratica exercícios físicos? "))
minutos_exercicios_mes = horas_exercicios_semana * 60 * 4
calorias_queimadas_mes = minutos_exercicios_mes * 5
print(f"O valor total de calorias queimadas em um mês é de {calorias_queimadas_mes} calorias.")