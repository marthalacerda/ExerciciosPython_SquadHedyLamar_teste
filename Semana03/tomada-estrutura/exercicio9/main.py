# Exercício 9
n = -1
n_pares = 0
n_impares = 0
n = int(input('Insira um número inteiro (ou 0 para sair): '))

# Loop
while n != 0:
    if n == 0:
        print('Fim do programa')
    elif n < 0:
        print('O número precisa ser positivo')
    elif n%2 == 0:
        n_pares += 1
    else:
        n_impares += 1
    
    n = int(input('Insira um número inteiro: '))

# Resultado
print(f'Foram inseridos {n_pares} números pares e {n_impares} números ímpares')