# 7. Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso.

idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida. Por favor, digite um valor positivo.")
elif idade <= 12:
    print(f"Sua idade é {idade}, você é criança.")
elif idade <= 17:
    print(f"Sua idade é {idade}, você é dolescente.")
elif idade <= 59:
    print(f"Sua idade é {idade}, você é adulto.")
else:
    print(f"Sua idade é {idade}, você é idoso.")