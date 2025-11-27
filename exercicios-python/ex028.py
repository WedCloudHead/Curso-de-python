#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario acertou ou nao

#como fiz:

import random  
numAleatorio = random.randint(0, 5)
print('O jogo de advinhação entre você e o computador, o computador escolhera um numero entre 0 e 5 e você precisa acertar qual numero o computador escolheu')

jogador = int(input('o computador já escolheu um numero, escolha o seu: '))

if numAleatorio == jogador:
    print(f'Parabens!! você acertou na mosca, a escolha do computador = {numAleatorio} sua escolha = {jogador}')
else:
    print(f'não foi dessa vez, o numero escolhido pelo computador foi: {numAleatorio}, tente de novo!')

    
#como professor demonstrou:

from random import randint #Importante importar somente o que for usar
from time import sleep #abaixo uma explicação so sobre esse import
pc = randint(0, 5) #faz o computador randomizar algum dos 5 numeros
print('-=-=-' * 15) #esse comando faz o print multiplicar por 20 o comando -=-
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-=-' * 15)
player = int(input('Em que numero eu pensei? ')) #player decide um numero
print('PROCESSANDO.. .. ..')
sleep(3)

if player == pc:
    print('PARABENS! Você me venceu!')
else:
    print(f'GANHEI! Eu pensei no numero {pc} e não no {player}')


#Sobre as linhas 21 e 28 a biblioteca time tem varios recursos interessantes, esse em especifico "sleep" funciona como um pause que o pc/terminal da pelo tempo que voce determinar antes de seguir para o proximo comando.
#para usa-lo é muito simples, basta encarar ele como um comando qualquer, ou seja primeiro voce ira importalo antes do comando ser dado no exemplo da linha 21 e depois basta chama-lo como na linha 28 sleep(3) e dentro do parenteses vai o numero equivalente a quantidade de segundos voce quer que o pc pause antes de seguir para o comando de baixo.