frase = str(input('Digite uma frase: '))
frase = frase.strip()
frase = frase.upper()

palavras1 = frase.split()
palavrascerto = ''.join(palavras1)

palavrasinvertidas1 = frase[::-1]
palavrasinvertidas = palavrasinvertidas1.split()
palavrasinvertidascerto = ''.join(palavrasinvertidas)

print('A frase \033[34m{}\033[m invertida é \033[34m{}\033[m'.format(palavrascerto, palavrasinvertidascerto))

if palavrascerto == palavrasinvertidascerto:
    print('Esta frase \033[34mÉ\033[m um Palindromo')
else:
    print('Esta frase \033[31mNÃO\033[m é um Palindromo')