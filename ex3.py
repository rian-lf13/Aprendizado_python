# Atividade

primeiro_valor = int(input('digite um valor:'))
segundo_valor = int(input('digite outro valor:'))

if primeiro_valor < segundo_valor:
    print(f'O valor {segundo_valor=} é maior que o valor {primeiro_valor=}.')
elif primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor=} é maior que o valor {segundo_valor=}.')
else:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais.')


#  Sistema de análise de benefícios

nome = str(input('Digite seu nome:'))
idade = int(input('Digite sua idade:'))
peso = float(input('Digite seu peso atual:'))
cart_estudante = (input('Possui carteira de estudante?'))

if cart_estudante == 'sim' or cart_estudante == 'Sim':
    print('Seus dados estão sendo analisados...')
else:
    print('Você não pode ter acesso aos benefícios.')




if 'e' in nome or 'E' in nome:
    print('Que legal! Seu nome contém a letra "e" maiuscula ou minuscula.')



imc = peso / (idade/10)**2

if imc > 25:
    print('Você não tem benefícios, seu peso está elevado.')
elif imc <= 25 or ('a' in nome or 'A' in nome):
    print('Benefícios disponiveis, mas você não pode participar de atividades especiais')
elif imc <= 25:
    print('Benefícios disponíveis! Você também tem acesso liberado as atividadades especiais')
else:
    print('Desculpe! Seus dados não atendem aos critérios.')