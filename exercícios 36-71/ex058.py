from random import randint
count = 1
n = int(input('Escreva um número de 1 a 10: '))
c = randint(0, 10)
if  n > 10 or n < 0:
    print('-=-' * 20)
    while n > 10 or n < 0:
        print('O número que digitou é inválido')
        n = int(input('Escreva um número: '))
        count += 1
if c != n and -1 < n <= 10:
    print('-=-' * 20)
    print(f'A sua jogada foi {n} e o computador jogou {c}')
    print('Não adivinhou! Tente de novo!')
    while c != n and -1 <n <=10:
        print('-=-' * 20)
        n = int(input('Escreva um número: '))
        c = randint(0, 10)
        print('A sua jogada foi {} e o computador jogou {}'.format(n, c))
        count += 1
if c == n:
    print('-=-' * 20)
    print('A sua jogada foi {} e o computador jogou {}'.format(n, c))
    print('Muito bem, adivinhou a jogada do Computador')

print('Foram precisas {} vezes para adivinhar o número!'.format(count))
print('-=-' * 20)


#solução aula


from random import randint
c = randint(0,10)
print('Tente adivinhar o número que pensei![0/10]: ')
acertou = False
palpites = 0
while not acertou:
    j = int(input('Qual é o seu palpite?'))
    palpites += 1
    if j == c:
        acertou = True
    else:
        if j < c :
            print('Mais... Tente novamente!')
        elif j > c:
            print('Menos... Tente novamente!')
print('Acertou com {} palpites !'.format(palpites))
