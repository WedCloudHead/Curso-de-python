#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a R$1.250,00 calcule um aumento de 10%
#para salarios inferiores ou iguais, o aumento é de 15%

from time import sleep
clt = float(input('qual valor do seu salario? '))
print('Se seu salarío for superior a R$1.250,00 seu aumento sera de 10%')
print('Se seu salarío for inferior a R$1.250,00 seu aumento sera de 15%')
print('CALCULANDO..')
sleep(3)
teto = float(1.250)
porcentagemTeto = (10)
porcentagemPiso = (15)
porcentagem = (100)
aumento_10 = (clt * porcentagemTeto / porcentagem)
aumento_15 = (clt * porcentagemPiso / porcentagem)

if clt > teto:
    print(f'seu aumento é 10%, equivalente a {aumento_10}')
    print(f'seu salario passa a ser {clt:.3f} + {aumento_10} reais')
else:
    print(f'seu aumento é de 15%, equivalente a {aumento_15}')
    print(f'seu salario passa a ser {clt:.3f} + {aumento_15} reais')