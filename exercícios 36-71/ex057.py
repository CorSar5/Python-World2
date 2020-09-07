s = str(input('Escreva o seu sexo [M/F]: ')).strip()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos. Por favor, informe o seu sexo ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(s))