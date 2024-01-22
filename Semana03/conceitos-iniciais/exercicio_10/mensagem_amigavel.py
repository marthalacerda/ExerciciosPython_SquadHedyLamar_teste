# 10. Faça um Programa que utilize 4 variáveis como preferir e no final print
# uma mensagem amigável utilizando as variáveis criadas.
# Exemplos de variáveis: nome, idade, lugar, profissão ....
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
# também e estou migrando de área.
# Lembrando que para o retorno vamos usar print com as variáveis
# criadas e este texto é somente um exemplo, utilizem a criatividade.

nome = input("Olá, me diga o seu nome: " )
cor = input("Me diga a sua cor favorita: ")
flor = input("Agora me diga uma flor que você goste muito: ")
numero = input("E por ultimo me diga um número de 1 até 10:")
print("")
print( f"Parabéns. {nome} você acaba de receber este buquê com {numero} {flor}, na cor {cor}.")

buque = """
               . .
    . .       . . .
 . . . .       . .     .
. . . .       . . .   . . .               ,
 . . . .     . . .     . .       _       d#D
. . . . .   . . . . ._. . .    _(%)_      `
   .     . . . . . _(#)_ .    (%%O%%)     "Bzzzz"
        . . . . _ (##O##) .   _ (%)   _
       . . .  _(#)_ (#)  . _ (%)_:  _(%)_
      . . . .(##O##)._\  _(#)%O%%):(%%O%%)
         . .   (#)  _  \(##O##))  |,'(%)
              `. ._(#)_ \,(#)  `. ;  _
                 (##O##) `.      Y _(#)_
                  .(#)\ . .).   / (##O##)
                 . . . `-.(. . ;  ,'(#)
                  . . . . .\. .| (
                 . . . d888888888888b
                  . . ,88888888888888b
                   . .d888888888888888
                    . d888888888888888
                     .`88888888888888P
                       Y8888888888888
                        Y8888888888P
_________________________`Y8888888P_____CJ_______
"""

print(buque)