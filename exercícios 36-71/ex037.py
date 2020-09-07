num = op = 0
while True:
    num = int(input('Digite um número inteiro [-1 para acabar programa]:'))
    if num == -1:
        break
    print('''Escolha uma das bases para conversão
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAl''')
    op = int(input('Sua opção:'))
    if op == 1:
        print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
    elif op == 2:
        print(f'{num} convertido para OCTAl é igual a {oct(num)[2:]}')
    elif op == 3:
        print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
    else:
        print('Opção inválida. Tente novamente')
print('Programa Encerrrado!')

