print('CÁLCULO DO IMC')
a = float(input('Indique a sua altura(em metros): '))
m = float(input('Indique o seu peso (arredondado às unidades do KG): '))
imc = m/(a**2)
print('O seu IMC é igual a {:.3f}'.format(imc))
if imc< 18.5:
    print('Você está abaixo do peso. Tente alimentar-se melhor mas de uma forma saudável!')
elif imc<25 :
    print('Muito bem está com o peso ideal! Continue assim')
elif imc<30 :
    print('Está acima do peso! Uma alimentação saudável conjugada de exercício diário, irá'
          ' coloca-lo num IMC saudável')
elif imc<40:
    print('O senhor está obeso, deverá consultar um nutricionista e melhorar o seu estilo de vida!')
else :
    print('Você sofre de obesidade mórbida, busque um profissional e tente mudar drásticamente o estilo de vida !!!!!')
