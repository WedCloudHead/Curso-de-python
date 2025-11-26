#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario acertou ou nao

import random  
numAleatorio = random.randint(0, 5)
print('O jogo de advinhação entre você e o computador, o computador escolhera um numero entre 0 e 5 e você precisa acertar qual numero o computador escolheu')
jogador = int(input('o computador já escolheu um numero, escolha o seu: '))
if numAleatorio == jogador:
    print(f'Parabens!! você acertou na mosca: {numAleatorio} = {jogador}')
else:
    print(f'não foi dessa vez, o numero escolhido pelo computador foi: {numAleatorio}')