def converta_para_celsius(temperatura):
    return (temperatura - 32) / 1.8

def converta_para_fahrenheit(temperatura):
    return (temperatura * 1.8) + 32

def script():
    opcao = input("Você deseja converter Celsius para Fahrenheit? Digite(s/n): ")

    if opcao == 's':
        temperatura = float(input("Digite a temperatura que deseja converter: "))
        resultado = converta_para_fahrenheit(temperatura)
        print(f"A temperatura em Fahrenheit é: {resultado:.1f}")
    
    opcao2 = input("Você deseja converter Fahrenheit para Celsius? Digite(s/n): ")

    if opcao2 == 's':
        temperatura = float(input("Digite a temperatura que deseja converter: "))
        resultado = converta_para_celsius(temperatura)
        print(f"A temperatura em Celsius é: {resultado:.1f}")

    else:
        return

def menu_conversao():

    while True:
        opcao_conversao = input('''Conversão Celsius/Fahrenheit
1-Converter Celsius para Fahrenheit
2-Converter Fahrenheit para Celsius
Digite o número referente à opção desejada: ''')

        if opcao_conversao == '1' or opcao_conversao == '2':
            break
    
    temperatura = float(input("Digite a temperatura que deseja converter: "))

    if opcao_conversao == '1':
        resultado = converta_para_fahrenheit(temperatura)
        print(f"A temperatura em Fahrenheit é: {resultado:.1f}")
    elif opcao_conversao == '2':
        resultado = converta_para_celsius(temperatura)
        print(f"A temperatura em Fahrenheit é: {resultado:.1f}")

script()
menu_conversao()
