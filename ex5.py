# Iterando com strings

nome=(input('Digite seu nome: '))

indice = 0

nova_cond=' '
while indice < len(nome):
    letra=(nome[indice])
    nova_cond+= f'*{letra}'
    indice += 1

print(nova_cond)
    