# Intrudução ao try/except

# numero = input('Vou dobrar o número que você digitar:')
# print(f'O número dobrado é {numero * 2}.')# nesse caso ocorre uma concatenção

# numero = float(input('Vou dobrar o número que você digitar:'))
# print(f'O número que você digitou é {numero} e ele dobrado é {numero*2:.2f}')

# numero_str = input('Vou dobrar o número que você digitar:')

# #try:
#     print('STR', numero_str)
#     numero_float= float(numero_str)
#     print('FLOAT', numero_float)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# except:
#     print('Isso não é um número')


# #ID- A identidade do valor que está na memória

# v1= 'Rian'
# print(id(v1)) 

''' tipos build-in, documentação, tipo imutaveis...
https://docs.python.org/pt-br/3/library/stdtypes.html
'''

''' Repetições 
while(enquanto)
'''

# condicao= True

# while condicao:
#     nome = input('Qual é o seu nome?')
#     print(f'O seu nome é {nome}')

#     if nome == 'sair':# ou seja, enquanto a pessoa não digitar sair vai ficar em loops.
#         break

# print('Acabou!')

# While em detalhes

# contador = 0

# while contador < 10:
#     print(contador) 
#     contador = contador + 1

# print('Acabou!')

# Operadores aritméticos de atribuição usando While

# contador = 0

# while contador < 10:
#     print(contador)
#     contador += 1

# print('Acabou!')

# While + continue

# contador = 0

# while contador < 10:
#     contador += 1

#     if contador == 4: #Aqui é o momento que o código pula
#         print('Não irei mostrar esse número.')
#         continue

#     print(contador)

#     if contador ==9: #nesse momento o código parou
#         break
# print('Acabou!')

# While + While (Laços internos)

qtd_linha = 5 
qtd_colunas = 5 

linha = 1

while linha <= qtd_linha:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou!')