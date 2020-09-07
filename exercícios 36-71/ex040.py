print('-=-'* 20)
print('\033[36mSeja bem-vindo à nossa aplicação de cáculo de médias finais\033[m')
print('Aqui, calcularemos a sua média e diremos se passará, terá de repetir o exame, ou passa.')
print('Serão então de 0-49 \033[31mreprovado\033[m, de 50-59 \033[33mrepetição da prova\033[m, de 60-100 \033[36maprovado\033[m')
print('-=-'* 20)
n1 = int(input('Digite sua \033[34mprimeira\033[m nota de 0-100: '))
n2 = int(input('Digite sua \033[31msegunda\033[m nota de 0-100: '))
m = (n1+ n2)/2
print(f'A sua médioa foi {m}.')
if m<50:
    print('Devia ter estudado mais, e ter sido um melhor aluno está \033[31mreprovado\033[m')
elif m>50 and m<60:
    print('Devia ter estudado mais!! Terá de \033[33mrepetir a prova\033[m')
elif m>= 60 and m<101:
    print('Parabéns!!Está \033[36maprovado\033[m')