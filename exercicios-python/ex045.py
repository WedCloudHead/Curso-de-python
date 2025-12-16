#Crie um programa que faça o computador jogar Jokenpô com você.

#Como eu fiz:

from random import randint 
from time import sleep
print('O FAMOSO JOGO DO JOKENPÔ VAI COMEÇAR, É SOMENTE VOCÊ CONTRA O COMPUTADOR!!!')
print('1 = (PEDRA) 2 = (PAPEL) 3 = (TESOURA)')
jogador = int(input('Escolha um dos três para disputar contra o computador: '))
print('O computador já escolheu o dele tambem!')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(0.8)

computador = randint(1, 3)
if jogador == 1 and computador == 2:
    print('(PEDRA X PAPEL)')
    print('O computador ganhou!!!')
elif jogador == 2 and computador == 3:
    print('(PAPEL X TESOURA)')
    print('O computador ganhou!!!')
elif jogador == 3 and computador == 1:
    print('(TESOURA X PEDRA)')
    print('O computador ganhou!!!')
elif jogador == 1 and computador == 3:
    print('PEDRA X TESOURA')
    print('O jogador ganhou!!!')
elif jogador == 2 and computador == 1:
    print('(PAPEL X PEDRA)')
    print('O jogador ganhou!!!')
elif jogador == 3 and computador == 2:
    print('(TESOURA X PAPEL)')
    print('O jogador ganhou!!!')
elif jogador == computador:
    print('(HOUVE UM EMPATE!!!)')
    print('Tente novamente.')
else:
    print('Essa é uma opção inválida, tente novamente!')
    

#Como professor demonstrou:

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
#print('O computador escolheu {}'.format(itens[comp]))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')  
jog = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jog]))
print('-=' * 11)
if comp == 0:
    if jog == 0:
        print('Empate')
    elif jog == 1:
        print('Jogador vence')
    elif jog ==2:
        print('Computador vence')
    else:
        print('Jogada inválida')

elif comp == 1:
    if jog == 1:
        print('Empate')
    elif jog == 2:
        print('Jogador vence')
    elif jog == 0:
        print('Computador vence')
    else:
        print('Jogada inválida')


elif comp == 2:
    if jog == 2:
        print('Empate')
    elif jog == 0:
        print('Jogador vence')
    elif jog == 1:
        print('Computador vence')
    else:
        print('Jogada inválida')





#Anotações:
#Eu estava em dúvida quando fiz meu programa se tinha alguma maneira de 
#transformar o randint do import que é em números para letras e sim, o 
#professor acabou de demonstrar na linha 50 com:
#.format(intens[comp])
#ele primeiro declara na linha 48 itens com 3 itens aleatórios e em 
#seguida cria esse .format 
#É possivel notar que nas linhas 63 e 64 é onde ocorre as transformações de
#itens[] numeros para as letras, é o mesmo processo da linha 50 porém como
#não tinha necessidade de deixar aquela linha no codigo eu só a tornei um 
#comentário.