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

# Operadores lógicos 


idade = 15 

if idade > 12 and 12 >idade:
    print('sim')
