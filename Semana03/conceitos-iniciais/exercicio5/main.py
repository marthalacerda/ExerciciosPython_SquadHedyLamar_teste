# 5. Escreva um programa que calcule o salário líquido. Lembrando de
# declarar o salário bruto e o percentual de desconto do Imposto de
# Renda.
# ● Renda até R$ 1.903,98: isento de imposto de renda;
# ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
# ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
# ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
# ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.

def calculaSalarioLiquido(renda, percentual):
  return renda - float("{:.2f}".format(renda * percentual /100))

renda = float(input('Informe a renda:\n'))

if renda <= 1903.98:
  print("Renda até R$ 1.903,98: isento de imposto de renda:\n", renda)

if renda >= 1903.99 and renda <= 2826.65:
  print("Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%:\n R$", calculaSalarioLiquido(renda, 7.5))


if renda >= 2826.66 and renda <= 3751.05:
  print("Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%:\n R$", calculaSalarioLiquido(renda, 15))


if renda >= 3751.06 and renda <= 4664.68:
  print("Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%:\n R$", calculaSalarioLiquido(renda, 22.5))

if renda > 4664.68:
  print("Renda acima de R$ 4.664,68:\n R$", calculaSalarioLiquido(renda, 27.5))




