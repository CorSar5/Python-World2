v = h = m = 0
print('-='*30)
print('Registro Pessoal')
print('-='*30)
while True:
    i = int(input('Escreva a sua idade: '))
    if i > 18:
        v += 1
    s = ' '
    while s not in 'MF':
        s = str(input('Indique o seu sexo [M/F]: ')).strip().upper()[0]
    if s == 'M':
        h += 1
    if s == 'F' and i<20:
        m += 1
    print('-=' * 30)
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    print('-=' * 30)
    if c == 'N':
        break
print(f'{v} pessoa(s) tinha(m) mais de 18 anos, foram registrados {h} homem/ns e {m} mulhere(s) tem menos de 20 anos!')
print('Programa Encerrado!')