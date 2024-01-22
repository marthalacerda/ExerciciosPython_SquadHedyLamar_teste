peso = float (input('Digite seu peso:'))
altura = float (input('Digite sua altura:'))


imc = peso/(altura**2)
imc_format= "{:.2f}".format(imc)
print("Seu IMC é de: ", imc_format);