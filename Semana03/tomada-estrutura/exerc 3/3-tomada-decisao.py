'''
Exercicios Tomada Decisão

3. Faça um programa que peça uma nota, entre 0 e 10. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''
nota = float(input('Digite a nota do aluno: '))

while (nota > 10) or (nota < 0):
    print('Informe um valor válido de 0 a 10.')
    nota = float(input('Digite a nota: '))
else:
    print(f'O valor da nota é válida: {nota:.1f}')
