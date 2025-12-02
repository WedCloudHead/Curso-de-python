#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a R$1.250,00 calcule um aumento de 10%
#para salarios inferiores ou iguais, o aumento é de 15%

#Como eu fiz:

from time import sleep
clt = float(input('qual valor do seu salario? '))
print('Se seu salarío for superior a R$1.250,00 seu aumento sera de 10%')
print('Se seu salarío for inferior a R$1.250,00 seu aumento sera de 15%')
print('CALCULANDO..')
sleep(2)
teto = float(1250)
porcentagemTeto = (10)
porcentagemPiso = (15)
porcentagem = (100)
aumento_10 = float(clt * porcentagemTeto / porcentagem)
aumento_15 = float(clt * porcentagemPiso / porcentagem)

if clt > teto:
    print(f'seu aumento é 10%, equivalente a {aumento_10:.2f}')
    print(f'seu salario passa a ser {clt + aumento_10:.2f} reais')
else:
    print(f'seu aumento é de 15%, equivalente a {aumento_15:.3f}')
    print(f'seu salario passa a ser {clt + aumento_15:.3f} reais') 


#Como professor demonstrou:

salario = float(input('Qual salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} agora, passa a ganhar R${novo:.2f}')



#Extra:
#é sempre bom ficar atento aos detalhes, o codigo feito pelo professor resolveu o problema de uma forma muito mais limpa e organizada que o meu, onde no meu caso eu gastei 17 linhas e tive que corrigir diversos erros de flutuaçao no meu codigo, enquanto o do professor com 5 linhas o problema esteve totalmente resolvido.