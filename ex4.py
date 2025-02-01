# Exercício 1

nome= str(input("digite seu nome: "))
idade = int(input("Digite sua idade:"))

if nome != '':
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome contém {len(nome)} caracteres')
    print(f'Seu nome tem "a"? {'a' in nome}')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else: 
    print('Desculpe! Você deixou os campos vazios.')

# Exercício 2

entrada = (input('Digite um número: '))

if entrada.isdigit():
    entrada_int= int(entrada)
    par_impar = entrada_int % 2 ==0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto ='par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print(f'Você não digitou um número inteiro')

# Exercício 
nome = str(input('Digite seu nome: '))
horario = int(input('Que horas são? (apenas o número das horas, 0-23):'))

if horario < 6:
    print(f'Boa Madrugada, {nome}!')
elif horario < 12:
    print(f'Bom dia, {nome}!')
elif horario < 18:
    print(f'Boa tarde, {nome}!')
elif horario < 24:
    print(f'Boa Noite, {nome}!')
else:
    print(f'Horário inválido!')

# Exercício

nome = str(input('Digite seu nome: '))

if nome <= nome[0:4]:
    print(f'{nome}, seu nome é curto.')
elif nome <= nome[0:6]:
    print(f'{nome}, seu nome é normal.')
elif nome > nome[0:6]:
    print(f'{nome}, seu nome é grande.')
else:
    print(f'Inválido')