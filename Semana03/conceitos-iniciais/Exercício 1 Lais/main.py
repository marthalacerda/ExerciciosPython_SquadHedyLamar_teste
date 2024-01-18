def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    try:
       return a / b
    
    except ZeroDivisionError:
        print("Impossível dividir pelo número 0")

def multiplicacao(a, b):
    return a * b

def main():
    numero1 = float(input("Insira o primeiro número: "))

    numero2 = float(input("Insira o segundo número: "))

    resultado_adicao = adicao(numero1, numero2)

    resultado_subtracao = subtracao(numero1, numero2)

    resultado_multiplicacao = multiplicacao(numero1, numero2)

    print(f"O resultado da adição dos dois números é: {resultado_adicao}")

    print(f"O resultado da subtração dos dois números é: {resultado_subtracao}")

    try:
        resultado_divisao = divisao(numero1, numero2)
    
    except ZeroDivisionError:
        print("Impossível dividir pelo número 0")
    
    print(f"O resultado da divisão dos dois números é: {resultado_divisao:.2f}")


    print(f"O resultado da multiplicacao dos dois números é: {resultado_multiplicacao}")

if __name__ == '__main__':
    main()