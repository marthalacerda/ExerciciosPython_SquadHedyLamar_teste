#cria uma lista com todas perguntas
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]

#cria uma lista para armazenar as respostas
respostas = []

#cria uma variavel soma com valor inicial 0
soma = 0

for pergunta in perguntas: #Percorre cada pergunta da lista perguntas
    resposta = input (pergunta + "Digite sim ou não: ") #Mostra a pergunta ao usuário e pede que responda sim ou não
    if resposta == "sim": #vefirica se a resposta é igual a sim
        soma += 1 #se a resposta foi sim, incrementa a soma em um

respostas.append(resposta) #adiciona cada resposta a lista de respostas


#cria uma lista com as possiveis classificacoes de participacao no crime
classificacao_partipacao_crime = ["Inocente", "Suspeita", "Cúmplice", "Cúmplice","Assassina"]

#caso a soma seja menor que 2, a classificacao é inocente, que corresponde ao item 0 da lista
if soma < 2:
    print(classificacao_partipacao_crime[0])

#senão, a classificacao é o item da lista correspondente a soma menos um, isso dá certo pois o primeiro item corresponde ao 0, por isso repetimos duas vezes o item cumplice, pois entre 3 e 4 respostas positivas é classificado como cumplice. Por esse motivo também temos o if, pois caso tivessemos 0 respostas positivas e subtraissemos 1, ia dar -1, que corresponde ao ultimo item da lista, sendo assim, daria uma resposta errada.
else:
    print(classificacao_partipacao_crime[soma-1])