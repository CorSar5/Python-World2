num = int(input('Primeiro termo: '))
r = int(input('Indique a razão da PA(Progressão Aritmética)'))
décimo = num +(10-1)*r
for c in range(num,décimo,r):
    print('{}'.format(c), end='->')
print('ACABOU')