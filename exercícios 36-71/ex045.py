from random import randint
from time import sleep
u = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opcões:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador =int(input('Qual a sua jogada? '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('-='*20)
print('Computador jogou {}'.format(u[computador]))
print('Jogador jogou {}'.format(u[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif  jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
         print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print('-='*20)