#melhore o jogo do desafio 028 onde o computador vai 'pensar' em um numero entre 0 a 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necesarios para vencer.


#Minha primeira resolução: DE PRIMEIRA PAPAI!!

from random import randint

pc = randint(0, 10)
jogador = None
tentativas = 0

print('O jogo vai começar, é vc contra o PC numa escolha de números de 0 a 10!!')
while jogador != pc:
    try:
        jogador = int(input('Digite o número que o pc pensou!: '))
        if jogador not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            print('Digite somente valores numericos entre 0 e 10!')
    
        if jogador == pc:
            print(f'Parabens você acertou! O Pc pensou em: {pc}!')
            print(f'O Player jogou: {jogador}!')
        else:
            tentativas += 1
    except ValueError:
        print('Digite apenas valores de 0 a 10')
print(f'O total de palpites dados foram {tentativas}')





#Como professor demonstrou:


from random import randint

computador = randint (0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print(f'Acertou com {palpites} tentativas. Parabéns!')

