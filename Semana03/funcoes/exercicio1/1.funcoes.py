'''
Exercícios de Funções

3. Faça um programa com uma função que necessite de três argumentos
e que forneça a soma desses três argumentos.
'''

def programa (x,y,z):
    soma = (x+y+z)
    return soma

x = float(input('Digite o valor1: '))
y = float(input('Digite o valor2: '))
z = float(input('Digite o valor3: '))

total = programa(x,y,z)
print(f'\n O valor total da soma é: {total}')
