soma = 0
cont = 0
print('Peço-lhe que me indique 6 números')
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num %2 ==0:
        soma += num
        cont += 1
print('Deu {} números pares e a soma dos números pares foi {}.'.format(cont,soma))