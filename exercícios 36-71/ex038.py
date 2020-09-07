print('Indique-me \033[31m três \033[m números.')
n1 = int(input('\033[35mDigite um número:\033[m '))
n2 = int(input('\033[35mDigite outro número (diferente ou igual)\033[m: '))
if n1> n2:
    print(f'O \033[34mmaior\033[m número é o {n1}, \033[36;40mprimeiro\033[m número digitado.')
elif n1<n2:
    print(f'O \033[34mmaior\033[m número é o {n2}, \033[31;40msegundo\033[m número digitado.')
else:
    print('\033[31mNão existe\033[m número maior, os números digitados são \033[33m iguais \033[m')