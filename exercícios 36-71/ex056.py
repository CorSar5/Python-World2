si = 0
m = 0
mh = 0
nv = ''
tm = 0
for p in range (1, 5):
    print('-------Informações {}ª pessoa-------'.format(p))
    n = str(input('Escreva o seu nome: ')).title().strip()
    i = int(input('Digite a sua idade: '))
    s = str(input('Diga o seu género [M/F]: ')).upper().strip()
    si += i
    if p == 1 and s in 'Mm':
        mh = i
        nv = n
    if s in 'Mm' and i > mh:
        mh = i
        nv = n
    if s in 'Ff' and i < 20:
        tm += 1
m = si / 4
print('A média de idade do grupo é de {} anos'.format(m))
print('O homem mais velho tem {} anos e chama-se {}'.format(mh,nv))
print('Existem {} mulheres com menos de 20 anos.'.format(tm))