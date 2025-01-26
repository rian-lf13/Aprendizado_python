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

# Programa de leitura de números impares e pares 

x = int(input('Digite um número:'))
result = x % 2

if result == 0: 
    print(f'O número {x} é par')
else:
    print(f'O número {x} é impar')

# Programa de leitura (maior e menor)

numero_1 = int(input('Digite um número:'))
numero_2 = int(input('Digite outro número:'))

if numero_1 < numero_2:
    print(f'O numero {numero_2} é maior que o número {numero_1}')
elif numero_2 < numero_1:
    print(f'O númeoro {numero_1} é maior que o número {numero_2}')
else:
    print('Esses números são iguais!')

# Categoria do lutador

lutador_nome= str(input('Digite seu nome: '))
peso = float(input('Digite seu peso atual: '))

if peso < 52:
    categoria = 'Inválida'
elif peso < 65:
    categoria = 'Pena'
elif peso  < 72:
    categoria = 'Leve'
elif peso  < 79:
    categoria = 'Ligeiro'
elif peso < 86:
    categoria = 'Meio-médio'
elif peso < 90:
    categoria = 'Médio'
elif peso <100:
    categoria = 'Meio-pesado'
elif peso < 120:
    categoria = 'Pesado'
else:
    categoria = 'Inválida'

msg= print(f'O lutador {lutador_nome}kg pesa {peso:.1f} e se enquadra na categoria {categoria}.')



    

 