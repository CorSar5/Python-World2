from datetime import date
print('-='*20+'-')
print('''  Bem-vindo à \033[31mConfederação Nacional de Natação\033[m
  Por favor indique abaixo o seu ano de nascimento para que lhe possamos dizer
em que categoria se deve inscrever''')
an = int(input('Indique o seu ano de nascimento:'))
at = date.today().year
i = at- an
print(f'O/A senhor/a tem {i} anos')
if i <= 9 and i >=0:
     print('Está situado na categoria \033[34mMIRIM\033[m.')
elif i <= 14:
    print('Está situado na categoria \033[33mINFANTIL\033[m')
elif i <= 19:
    print('Está na categoria \033[36mJUNIOR\033[m')
elif i <= 20:
    print('Está na categoria \033[31mSÉNIOR\033[m')
else:
    print('Está na categoria \033[32mMASTER\033[m')