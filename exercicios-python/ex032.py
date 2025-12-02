#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

#Como eu fiz:

ano_bissexto = int(input('Digite um ano e descubra se ele é bissexto ou não: '))
bissexto = ano_bissexto % 4

if bissexto == 0:
    print('Este ano é bissexto')
else:
    print('Este ano não é bissexto')


#Como o professor demonstrou:
from datetime import date
ano = int(input('Que ano voce quer analizar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')


#Extra:

#Sobre as linhas 15, 17 e 18 o que rolou aqui foi um import da biblioteca python : https://docs.python.org/3/library/datetime.html é a biblioteca relacionada a datas, tempo e etc.. basicamente na linha 15 houve a import especifico dessa bibliotrca: 'from datetime import date' e nas linhas 17 e 18 é onde é criado uma condição simples somente para utilizar do import entao basicamente: if ano == 0: (ou seja se o usuario digitatar 0) significa que ele quer saber sobre o ano atual no qual esta configurado a maquina dele. linha 18 diz ano = date.today().year ou seja, se ele digitar zero, ano vai receber o import de hoje e somente o ano. e os print nas linhas 20 e 22 ja introduzem esse import automaticamente pois no print é pedido a declaração ano. 


#Na linha 18 temos alguns termos interessantes que não vimos muito ainda
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#and  tambem pode ser entendido como 'e tambem'. 
#!=  tambem pode ser entendido como 'diferente' ou 'não igual'.
#or  tambem pode ser lido como 'ou' ou 'ou entao'.

#nesse caso essa linha se leria assim: (se) o ano dividido por 4 for == 0 (e tambem) ano dividido por 100 for (diferente) de 0 (ou) ano dividido por 400 for == 0

