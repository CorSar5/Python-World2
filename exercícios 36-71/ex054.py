cont = 0
som = 0
for c in range(1, 8):
    idade = int(input('Digite a sua idade: '))
    if idade < 21:
        cont += 1
    else:
        som += 1
if som == 7:
    print('Neste grupo todos tem a maioridade!')
elif som<7 and cont<7 :
    print('Existem {} pessoas com a maioridade.'.format(som))

if cont == 7:
    print('Neste grupo ninguém tem a maioridade')
elif cont<7 and som<7:
    print('Existem {} pessoas sem a maioridade.'.format(cont))