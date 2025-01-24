# Informar dados

nome= input(('Qual o seu nome?'))
sobrenome=input(('Qual o seu sobrenome?'))


idade = int(input('Informe a sua idade:'))
data_nasc= input('Qual sua data de nascimento?')
maior_idade= idade >= 18

altura= float(input('Qual sua altura atual?'))

print('Me chamo', nome, sobrenome,'tenho', altura, 'nasci no dia', data_nasc, 'tenho', idade, 'anos, ja sou maior de idade?', maior_idade)

# Calculadora de média e verificação de aprovação

aluno_nome= str(input('Digite seu nome:'))

nota_bi1= float(input('Digite sua nota:'))
nota_bi2= float(input('Digite sua nota:'))
nota_bi3= float(input('Digite sua nota:'))

primeira_nota= nota_bi1 * 3 
segunda_nota= nota_bi2 * 4
terceira_nota= nota_bi3 * 5

media_aluno= (primeira_nota + segunda_nota + terceira_nota) / 12

print(f'{aluno_nome} sua nota do primeiro bimestre é {float(nota_bi1):.2f}, do segundo bimestre é {float(nota_bi2):.2f}, do terceiro bimestre é {float(nota_bi3):.2f}.', end='   ')

if media_aluno >= 6:
    print(f'Status: (Aprovado!!!) Sua media é: {media_aluno:.2f}')
elif media_aluno < 5.99:
    print(f'Status: (Reprovado!!!) Sua media é: {media_aluno:.2f}')

# Cálculo de desempenho em vendas 

nome_vendedor= str(input('digite seu nome:'))
 
mes_venda0= float(input('digite o valor total de vendas desse mês:'))
mes_venda1= float(input('digite o valor total de vendas desse mês:'))
mes_venda2= float(input('digite o valor total de vendas desse mês:'))

media_tri_vendas= (mes_venda0 + mes_venda1 + mes_venda2) / 3

if media_tri_vendas > 10.000 :
    print(f'Excelente, {nome_vendedor}!!! Você vendeu no mês de Janeiro R${mes_venda0:.3f}, em Fevereiro R${mes_venda1:.3f} e em Março R${mes_venda2:.3f}')
elif media_tri_vendas >=7.000 :
    print(f'Bom, {nome_vendedor}!!! Você vendeu no mês de Janeiro R${mes_venda0:.3f}, em Fevereiro R${mes_venda1:.3f} e em Março R${mes_venda2:.3f}')
elif media_tri_vendas < 7.000 :  
    print(f'Infelizmente, {nome_vendedor}, você não bateu sua meta. Você vendeu no mês de Janeiro R${mes_venda0:.3f}, em Fevereiro R${mes_venda1:.3f} e em Março R${mes_venda2:.3f}')


print(f'Sua média nos últimos três meses foi de R${media_tri_vendas:.3f}')




 






