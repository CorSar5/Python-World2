f = int(input('Digite o número que quer efetuar o fatorial: '))
c = f
n = 1
print('Calculando {}! = '.format(f), end= '')
while c> 0:
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end='')
    n *= c
    c-=1
print('{}'.format(n))