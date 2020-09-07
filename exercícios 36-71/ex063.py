print('-'*30)
t1 = 0
print('Sequência de Fibonacci')
print('-'*30)
t2 = 1
n = int(input('Quantos termos quer mostrar? '))
print('-'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont<= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('\nFIM')