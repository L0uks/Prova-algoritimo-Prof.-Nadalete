salario = float(input('Informe o salario R$ '))
vendas = float(input('Valor das vendas R$ '))
total = salario + vendas
total2 = total - 1500
c = total + (total * 5)/100
if total <= 1500:
    print('Salario a receber é R$ {:.2f}'.format(c))
elif total > 1500:
    t = c + (total2 * 7)/100
    print('Salario a receber R$ {:.2f}'.format(t))