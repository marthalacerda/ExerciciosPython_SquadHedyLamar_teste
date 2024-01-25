print('-' * 30)
print('*** ORDENANDO 3 NÚMEROS ***')
print('-' * 30)

# Lista para armazenar os numeros:
numeros = []

# Laço de repetição para pedir os números com tratamento de erro:
for i in range(3):
  while True:
      try:
        numero = int(input(f'Digite o número {i + 1}: '))
        numeros.append(numero)
        break
      except ValueError:
        print('\33[1;31m(!) Erro:\33[m Por favor, digite um número inteiro.') 


# 1) ordenando os números com sorted():     

listaOrdenada = sorted(numeros)

# 2) ordenando os números com if:

# primeiro e segundo número trocam de posição se o primeiro for maior que o segundo
if numeros[0] > numeros[1]:
   numeros[0], numeros[1] = numeros[1], numeros[0]
# comparação com a segunda e terceira posição
if numeros[1] > numeros[2]:
   numeros[1], numeros[2] = numeros[2], numeros[1]
# comparação novamente com primeira e segunda posição, caso tenha havido troca entre a segunda e terceira posição
if numeros[0] > numeros[1]:
   numeros[0], numeros[1] = numeros[1], numeros[0]


# Mostrando na tela:
print('-' * 30)

print('Os números em ordem crescente com \033[1;32msorted()\033[m:' )
print(f'{listaOrdenada[0]} < {listaOrdenada[1]} < {listaOrdenada[2]}')

print('Os números em ordem crescente com \033[1;32mif\033[m:')
print(f'{numeros[0]} < {numeros[1]} < {numeros[2]}')
