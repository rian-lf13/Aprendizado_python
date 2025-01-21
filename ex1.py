nome= input(('Qual o seu nome?'))
sobrenome=input(('Qual o seu sobrenome?'))


idade = int(input('Informe a sua idade:'))
data_nasc= input('Qual sua data de nascimento?')
maior_idade= idade >= 18

altura= float(input('Qual sua altura atual?'))

print('Me chamo', nome, sobrenome,'tenho', altura, 'nasci no dia', data_nasc, 'tenho', idade, 'anos, ja sou maior de idade?', maior_idade)

