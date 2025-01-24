# Função INPUT

nome = str(input('Qual é o seu nome?'))
print(f'Meu nome é {nome}') #nome= para checar onde está aparecendo a mesnagem da variável

# Condicionais (IF, ELIF e ELSE)


idade = int(input('Informe a sua idade:'))

if idade <12 :
    print('Você ainda é uma criança!')
elif idade < 18:
    print('Você é adolescente!')
elif idade < 50:
    print('Você está na fase adulta')
elif idade <100: 
    print('Ah, a idade chegou...')
else:
    print('Você é um dinossauro!')

# Operadores lógicos (Operador and)


idade = 15 

if idade > 12 and 12 >idade:
    print('sim')

# Operadores lógicos (Operador or)

caderno = 500

if caderno != 500 or caderno > 1000:
    print("Seu caderno tem mais de 100 folhas")
elif caderno:
    print("Seu caderno tem menos folha do que a comparação")

# Operadores lógicos (Operador not)

senha = int(input("informe a senha:"))

if senha != "123456":
    print("senha incorreta!")

# Operadores lógicos (Operador in e not in)


var_1= 'Rian'

print('a' in var_1)


