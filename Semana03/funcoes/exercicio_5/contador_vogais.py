def contar_vogais(frase):
  qtd_vogais = 0
  frase_colorida = ''
  for letra in str(frase).strip():
    if letra.lower() in 'aãäáàâeëéèêiïíìîoõöóòôuüúùû':
      qtd_vogais += 1
      frase_colorida += f'\033[32m{letra.upper()}\033[m'
    else:
      frase_colorida += letra.lower()
  print()    
  print(f'Quantidade de vogais na frase digitada: {qtd_vogais}')
  if qtd_vogais > 0:
    print(f'{frase_colorida}')
  print()

# Programa:
print('-' * 30)
print('*** CONTADOR DE VOGAIS ***')
print('-' * 30)
contar_vogais(input('Digite uma frase, por favor: '))
