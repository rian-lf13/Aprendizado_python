primeiro_valor = int(input('digite um valor:'))
segundo_valor = int(input('digite outro valor:'))

if primeiro_valor < segundo_valor:
    print(f'O valor {segundo_valor=} é maior que o valor {primeiro_valor=}.')
elif primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor=} é maior que o valor {segundo_valor=}.')
else:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais.')