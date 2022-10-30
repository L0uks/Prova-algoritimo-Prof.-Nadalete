paisA = 15000
paisB = 45000
paisC = 65000
ano = 0

while paisA <= paisB:
    paisA = paisA + (paisA * 10)/100
    paisB = paisB + (paisB * 5)/100
    ano = ano + 1
print('A população A se igualara ou utrapassara a população B em {} anos '.format(ano))

paisA = 15000
paisB = 45000
paisC = 65000
ano2 = 0
while paisA <= paisC + (paisC * 23)/100:
    paisA = paisA + (paisA * 10) / 100
    paisC = paisC + (paisC * 2.5) / 100
    ano2 = ano2 + 1
print('A população A utrapassara a população C em 23% em  {} anos '.format(ano2))
