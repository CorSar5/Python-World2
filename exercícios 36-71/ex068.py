from random import randint
c = j = comt = 0
pi = ''
print('-='*30)
print('Vamos jogar ao PAR ou ÍMPAR!')
print('-='*30)
while True:
    j = int(input('Digite um número: '))
    pi = str(input('Deseja Par ou Ímpar?[P/I] ')).upper().strip()
    c = randint(1, 10)
    jun = (j + c) % 2
    print(f'Você escolheu {j} e o computador {c}.O resultado foi {c + j}')
    if jun == 0 and pi in 'pP':
        print('É realmente um número PAR')
        print('-=' * 30)
        print('Você VENCEU!')
        print('-=' * 30)
        comt += 1
    if jun != 0 and pi in 'iI':
        print('É realmente um número ÍMPAR')
        print('-=' * 30)
        print('Você VENCEU!')
        print('-=' * 30)
        comt += 1
    if jun == 0 and pi in 'iI' or jun != 0 and pi in 'Pp':
        break
print(f'Você Perdeu! Acabou o jogo com {comt} rondas ganhas!')


#solução aula

from random import randint
v = 0
while True:
    print('-=' * 30)
    jogador = int(input('Escreva um número: '))
    computador = randint(0,10)
    total = computador + computador
    print('-=' * 30)
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.',end = '')
    print('DEU PAR'if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v+= 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 ==1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Ganhaste com {v} vitórias')
