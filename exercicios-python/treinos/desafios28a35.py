#28 Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario acertou ou nao

from random import randint
from time import sleep
print('O pc escolhera um numero entre 0 e 5, tente advinhar!')
usuario = int(input('Digite agora para descobrir: '))
print('Pc está pensando...')
sleep(2)
comp = randint(1, 5)
if usuario == comp:
    print(f'Parabens! Você acertou na mosca! pc:{comp} = vc:{usuario}')
else:
    print(f'Que pena! O valor escolhido pelo pc foi {comp}')

#Correção: está correto




#29 Escreva um programa que leia a velociadade de um carro.
#se ele ultrapassar 80k/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$7,00 por km acima do limite


vel = float(input('A que velocidade está o carro? '))
if vel > 80:
    print('Você excedeu o limite de velocidade!')
    multa = (vel - 80) * 7
    print(f'Sua multa é de {multa:.2f}')
else:
    print('Você está dentro do limite de velocidade de 80km/h')
print('Dirija com segurança!')


#Correção: está correto



#30 Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar


num = int(input('Digite um numero qualquer para descobrir se ele é impar ou par: '))
resultado = num % 2
if resultado == 0:
    print('Seu numero é par!')
else:
    print('Seu numero é impar!')
print('Fim!')


#Correção: está correto



#31 Desenvolva um programa que pergunte a distancia de uma viagem em km. 
#calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas



viagem = float(input('Diga a distancia da viagem em km: '))
passagem200km = viagem * 0.50
passagem_maior = viagem * 0.45
if viagem <= 200:
    print(f'Sua viagem custara {passagem200km:.2f} no total')
else:
    print(f'Sua viagem custara {passagem_maior:.2f} no total')


#Correção: está correto



#32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto


from datetime import date
ano = int(input('Diga um ano para saber se ele é bissexto: ')) 
if ano == 0:
    ano = date.year()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim esse ano é bissesto!')
else:
    print('O ano informado não é bissexto!')

#Correção: está correto




#33 Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor 


num = int(input('Digite um numero:'))
num01 = int(input('Digito segunddo numero: '))
num02 = int(input('Digite o terceiro numero: '))
menor = num
if num01<num and num01<num02:
    menor = num01
if num02<num and num02<num01:
    menor = num02
maior = num
if num01>num and num01>num02:
    maior = num01
if num02>num and num02>num01:
    maior = num02
    print(f'O maior valor digitado foi {maior}')
    print(f'O menor valor digitado foi {menor}')
else:
    print('Todos os valores são iguais!')


#Correção: está correto



#34 Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a R$1.250,00 calcule um aumento de 10%
#para salarios inferiores ou iguais, o aumento é de 15%


salario = float(input('Qual seu sálario? '))
aumento10 = (salario * 10) / 100
aumento15 = (salario * 15) / 100

if salario > 1250:
    print(f'Seu salario é superior a 1.250,00 e seu aumento é de 10% do valor atual, seu aumento é de: {aumento10:.2f} ficando {salario + aumento10:.2f} ')
if salario <= 1250:
    print(f'Seu salario é igual ou inferior a 1.250,00 e seu aumento é de 15% do valor atual, seu aumento é de: {aumento15:.2f} ficando {salario + aumento15:.2f} ')


#Correção: está correto




# 35 Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo 


reta01 = int(input('Diga o valor da primeira reta: '))
reta02 = int(input('Diga o valor da segunda reta: '))
reta03 = int(input('Diga o valor da terceira reta: '))
if reta01 < reta02 + reta03 and reta02 < reta01 + reta03 and reta03 < reta01 + reta02:
    print(f'Os valores dados podem sim formar um triangulo {reta01}, {reta02}, {reta03}')
else:
    print(f'Os valores dados não podem formar um triangulo: {reta01}, {reta02}, {reta03}')



#Correção: está correto
