n = 0
print('-='*30)
while True:
    n = int(input('Qual é o número que quer saber a tabuada [número negativo para encerrar]: '))
    if n<0:
        break
    for c in range(1,11):
        f = n * c
        print(f'{c}*{n}={f}')
print('-='*30)
print('Programa Encerrado!')