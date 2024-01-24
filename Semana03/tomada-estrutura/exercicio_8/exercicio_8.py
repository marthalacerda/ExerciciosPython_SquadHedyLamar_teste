# 8. Criar um programa em Python que solicite três números ao usuário, utilize
# estruturas condicionais para determinar o maior entre eles e apresente o
# resultado.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    maior_numero = numero_1
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    maior_numero = numero_2
else:
    maior_numero = numero_3

print(f"O maior número entre {numero_1}, {numero_2} e {numero_3} é: {maior_numero}")