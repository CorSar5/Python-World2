n = 0
cont = 0
n1 = 0
n = int(input('Escreva um número [999 para parar]: '))
while n != 999:
    cont += 1
    n1 += n
    n = int(input('Escreva um número [999 para parar]: '))
print('Foram digitados {} números e a sua soma deu {}'.format(cont, n1))