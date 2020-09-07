from datetime import date
print('\033[30mBem-vindo\033[m ao \033[31mrecrutamento\033[m \033[33mmilitar\033[m \033[32mPortuguês\033[m')
a = int(input('\033[36mEscreva o ano em que nasceu:\033[m '))
at = date.today().year
i = at-a
if i>= 18 and i<= 27:
    print('Tem a idade \033[34mideal\033[m para se alistar nas \033[31mforças armadas\033[m')
elif i< 18 :
    p= 18-i
    print(f'\033[31mAinda não tem idade para se alistar nas forças armadas\033[m, faltam ainda {p} anos')
elif i>27 :
    t = i-27
    print(f'\033[31mJá não se poderá inscrever nas forças armadas\033[m a sua idade execede {t} anos o limite.')