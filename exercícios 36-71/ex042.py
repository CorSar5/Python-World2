print('Pedir-lhe-ei para me dar três comprimentos, e se estes conseguem formar um triângulo:')
print('-_-'*20)

cores = {'reset':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
          'verde': '\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo': '\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[37m',
         'preto':'\033[7;30m'}

a = float(input('{}Primeira medida{}: '.format(cores['ciano'],cores['reset'])))
b = float(input('{}Segunda medida{}: '.format(cores['ciano'],cores['reset'])))
c = float(input('{}Terceira medida{}: '.format(cores['ciano'],cores['reset'])))

print('-_-'*20)
if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b:
     print('Sim com as medidas: {}, {} e {} {}é{} {}possível{} formar um triângulo'.format(a,b,c,cores['roxo'],cores['reset'],cores['ciano'],cores['reset']))
     if  a == b == c :
            print('Este triângulo será {}equilátro{}!'.format(cores['vermelho'],cores['reset']))

     if a== b and b!=c or b==c and c!=a or  a==c and c!=b:
            print('Este triângulo será {}isósceles!{}'.format(cores['azul'],cores['reset']))

     if  a!=b!=c:
            print('Este triângulo será {}escaleno{}!'.format(cores['verde'], cores['reset']))


else:
    print('Não, com as medidas {}, {} e {} {}não é possível{} formar um triângulo'.format(a,b,c, cores['vermelho'], cores['reset']))
print('-_-'*20)