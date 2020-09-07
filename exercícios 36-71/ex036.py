vc = int(input('Indique o valor da casa que pretende construir: '))
s = float(input('Indique o valor do(s)  salário(s) que recebe(m): '))
a = int(input('Número de anos que irá querer pagar a casa: '))
p = a*12
sa = s*0.3
if sa * p >= vc:
    print('Com o seu salário de {} e com o valor da casa que é de {}, em {} anos irá pagar a casa pagando 30% do seu ordenado'.format(s,vc, a))
    print(':.-.:'*15)
    print('O empréstimo será cedido!')
else:
    print(f'O empréstimo será negado 30% do seu salário não pagará o valor da casa em {a} anos')