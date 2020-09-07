c = q = menor = 0
g = ''
while True:
    print('-=' * 30)
    n = str(input('Nome do produto: '))
    p = float(input('Indique o preço do produto: '))
    q += p
    print('-=' * 30)
    ss = ' '
    while ss not in 'SN':
        ss = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if p > 1000:
        c += 1
    if ss == 'N':
        break
    p = menor
    if c == 1 or p < menor:
        menor = p
        g = n
print(f'O total gasto foi de {q}')
print(f'Existem {c} produtos que custam mais de 1000€.')
print(f'O produro mais barato é o {g} que custa {menor}€.')