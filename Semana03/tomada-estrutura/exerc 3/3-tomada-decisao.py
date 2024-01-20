'''
Exercicios Tomada Decisão

3. Faça um programa que peça uma nota, entre 0 e 10. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''
nota = float(input('Digite a nota: '))

if (nota <= 10) and (nota >= 0):
    print(f'O valor da nota é válida: {nota:.1f}')
    
else:
    print('Informe um valor válido de 0 a 10.')
    
