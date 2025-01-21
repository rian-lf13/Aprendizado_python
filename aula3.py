nome= str('Rian')
altura= float(1.81)
peso= float(80.0)

# Introdução à formatação de strings

print(f'Meu nome é {nome}, tenho {altura}m de altura e peso {peso}kg.')


#  Formatação de strings com o método format

a= 'A'
b= 'b'
c= 1.1
string= 'a={nome1} b={nome2} b={nome2} b={nome2} c={nome3:.2f}'
formato=string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)