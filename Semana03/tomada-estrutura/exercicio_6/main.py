def login(nome, senha):
    if nome == "admin" and senha == "admin123":
        print("Acesso permitido")
        return
    else:
        print("O nome e/ou senha estão incorretos")
        return

def main():

    nome = input("Login: ")
    senha = input("Senha: ")

    login(nome, senha)

if __name__ == "__main__":
    main()