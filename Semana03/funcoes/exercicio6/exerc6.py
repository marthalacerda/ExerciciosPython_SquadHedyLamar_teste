# Importar a biblioteca random
import random

# Definir uma lista de palavras possíveis
palavras = ["banana", "maçã", "laranja", "abacaxi", "manga"]

# Escolher uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

# Inicializar uma lista de espaços em branco com o mesmo tamanho da palavra secreta
palavra_exibida = ["_" for letra in palavra_secreta]

# Definir o número máximo de tentativas
tentativas = 6

# Definir uma variável para indicar se o jogo terminou
fim_de_jogo = False

# Imprimir uma mensagem de boas-vindas
print("Bem-vindo ao jogo da forca!")
print("A palavra secreta tem", len(palavra_secreta), "letras.")

# Enquanto o jogo não terminar, repetir os seguintes passos
while not fim_de_jogo:

    # Imprimir a palavra exibida com espaços entre as letras
    print(" ".join(palavra_exibida))

    # Pedir ao jogador que digite uma letra
    letra = input("Digite uma letra: ").lower()

    # Verificar se a letra está na palavra secreta
    if letra in palavra_secreta:

        # Se sim, revelar as posições correspondentes na palavra exibida
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_exibida[i] = letra

        # Imprimir uma mensagem de acerto
        print("Você acertou uma letra!")

    else:

        # Se não, diminuir o número de tentativas em 1
        tentativas -= 1

        # Imprimir uma mensagem de erro
        print("Você errou! Você tem", tentativas, "tentativas restantes.")

    # Verificar se o jogador acertou toda a palavra
    if "_" not in palavra_exibida:

        # Se sim, imprimir uma mensagem de vitória e encerrar o jogo
        print("Parabéns, você ganhou! A palavra era", palavra_secreta + ".")
        fim_de_jogo = True

    # Verificar se o jogador excedeu o número máximo de tentativas
    elif tentativas == 0:

        # Se sim, imprimir uma mensagem de derrota e encerrar o jogo
        print("Você perdeu! A palavra era", palavra_secreta + ".")
        fim_de_jogo = True
