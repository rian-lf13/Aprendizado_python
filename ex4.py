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

