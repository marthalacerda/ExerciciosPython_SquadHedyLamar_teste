valorHora = float (input('Quanto você ganha por hora? : '))
totalHoraMensal = float (input('Digite o total trabalhado no ultimo mês:'))

valorRecebido = valorHora * totalHoraMensal

valorRecebidoFormatado= "{:.2f}".format(valorRecebido)
print("Você receberá o total de: ", valorRecebidoFormatado);