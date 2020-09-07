n = int(input('Escreva um número: '))
if n % 2 == 0 or n % 3 == 0 or n % 5== 0 or n % 7 == 0:
    print('Esse número {} não é um número primo'.format(n))
else:
    print('O número {} é um número primo'.format(n))