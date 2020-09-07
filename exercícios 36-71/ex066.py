n = s = c = 0
while True:
    n = int(input('Escreva um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você escreveu {c} números e a sua soma foi {s}!')