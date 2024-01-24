notas = {}
notasLista =[]
alunos = 0
qtdAlu = 0
media = 0
soma = 0
i=0


while alunos < 2:
    soma = 0
    print('aluno:',alunos+1)
    while i < 4 :
        nota = float(input('Digite sua nota entre 0 e 10 '))
        if nota > 0 and nota <= 10:
            soma = soma + nota 
            i+=1
    media = soma /4    
    if media >= 7:
        notasLista.append(media)
        qtdAlu +=1 
    notas.update({f'aluno {alunos+1}':media})
    alunos +=1
    i=0   
    
print('Quantidade de alunos com media maior ou igual a 7.0: ',qtdAlu)
print('Todas as médias',notas)