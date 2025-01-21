# Calculo de IMC

nome= str(input('Qual é o seu nome?'))
altura= float(input('Qual a sua altura?'))
peso= float(input('Quantos quilos você tem?'))

imc= peso / (altura * altura)

# Introdução à formatação de strings
print(f'Meu nome é {nome}, tenho {altura:.2f}m de altura, atualmente estou pesando {peso} e meu IMC, é: {imc:.2f}')

