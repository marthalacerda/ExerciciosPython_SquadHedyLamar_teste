contatos = {
    "Ana": "11-4435-5657",
    "Beatriz": "13-4459-4793",
    "Carlos": "11-4676-9894",
    "Diogo": "11-94873-6456",
    "Fernanda": "21-5678-4547",
    "Gabriela": "35-3475-7834",
    "Helena": "11-90345-8723"
}

def procurar_contato():
    
    nome = input("Digite o nome do contato que deseja procurar: ")

        
    # Procura no dicionário contatos o nome digitado pelo usuário
    for i in contatos:
        # Se o nome é encontrado, imprime na tela e retorna a função
        if nome == i:
            print(f"O telefone de {nome} é {contatos[nome]}")
            return
    
    # Depois de ter procurado todo o dicionário contatos, sem achar o nome, imprime a mensagem
    print("O nome procurado não consta na lista de contatos")
        
        
# Chama a função
procurar_contato()