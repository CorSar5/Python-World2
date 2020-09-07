n = 0
q = 'S'
maior = menor = n1 = cont = 0
while q  in 'Ss':
    n = int(input('Escreva um número: '))
    cont += 1
    n1 += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    q = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
m = n1 / cont
print('Você escreveu {} números e a média foi {} \n O maior valor foi {} e o menor foi {}'.format(cont, m, maior, menor))