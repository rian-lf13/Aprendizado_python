# # Função INPUT

# nome = str(input('Qual é o seu nome?'))
# print(f'Meu nome é {nome}') #nome= para checar onde está aparecendo a mesnagem da variável

# # Condicionais (IF, ELIF e ELSE)


# idade = int(input('Informe a sua idade:'))

# if idade <12 :
#     print('Você ainda é uma criança!')
# elif idade < 18:
#     print('Você é adolescente!')
# elif idade < 50:
#     print('Você está na fase adulta')
# elif idade <100: 
#     print('Ah, a idade chegou...')
# else:
#     print('Você é um dinossauro!')

# # Operadores lógicos (Operador and)


# idade = 15 

# if idade > 12 and 12 >idade:
#     print('sim')

# # Operadores lógicos (Operador or)

# caderno = 500

# if caderno != 500 or caderno > 1000:
#     print("Seu caderno tem mais de 100 folhas")
# elif caderno:
#     print("Seu caderno tem menos folha do que a comparação")

# # Operadores lógicos (Operador not)

# senha = int(input("informe a senha:"))

# if senha != "123456":
#     print("senha incorreta!")

# # Operadores lógicos (Operador in e not in)


# var_1= 'Rian'

# print('a' in var_1)

# # Interpolação básica de strings

# nome= 'Luiz'
# preco= 1000.958976643
# var = '%s, o preço total é R$%.2f' % (nome, preco)

# print(var)
# print('Hexadecimal de %d é %08x' % (15,15))

""" Formatação básica de strings

s - strings 
d - int
f - float

<Numero de dígitos>f
x ou X- Hexadecimal 
(Caractere)(<>^)(Quantidade)
> - Esquerda 
< - Direita
^ - Centro 
= força p número a aprecerantes dos zeros 
Sinal de - + ou - 
Ex.: >-100,.1f
Colnversion flags - !r !s !a
"""
var = 'rian'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}...')
print(f'{15679:,.1f}')

print(f'{-15679:+}') # Serve para aparecer quando o número for positivo ou negativo

print(f'{3151.634811500:0=10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

"""
Fatiamento de strings 
012345678
"""
