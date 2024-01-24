# 4. Implemente um programa que classifique um aluno com base em sua
# pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
# a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
# reprovado.

pontuacaoValida = False

while pontuacaoValida == False:
      
    pontuacao = float(input('Informe a pontuação:\n'))

    if pontuacao < 7:
        print("Aluno Reprovado")
        pontuacaoValida = True
    elif pontuacao >= 7 and pontuacao <= 10:
        print("Aluno Aprovado!")
        pontuacaoValida = True
    else:
        print("Pontuação inválida!")



