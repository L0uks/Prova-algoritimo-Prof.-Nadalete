sequen = 1
cont = 0
sequen2 = 1
cont2 = 1
pnum = 0

for c in range(10):
    c = c + 1
    num = int(input('Digite um numero: '))
    if c != 0:
        if num > pnum:
            cont += 1
            if cont > sequen:
                sequen = cont
        elif num == pnum:
            cont2 += 1
            if cont2 > sequen2:
               sequen2 = cont2
        pnum = num

print('O tamanho da maior sequencia concecutiva é {}'.format(cont))
print('O tamanho da maior sequencia constante é {} '.format(cont2))