#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vítórias consecutivas que ele conquistou no final do jogo.


#Primeira bosta de tentativa: :)


from random import randint

jogador = 0
total_vitorias = 0

while True:
    computador = randint
    try:
        jogador = int(input('Escolha impar ou par: '))
        break
    except ValueError:
        print('Digite apenas números')

    if jogador / 2 == 0 and computador / 2 == 0:
        jogador = True
        print('Vitoria do jogador')
        total_vitorias += 1
    elif jogador / 2 == 1 and computador / 2 == 1:
        jogador = True
        print('Vitoria do jogador')
        total_vitorias += 1
    else:
        if jogador / 2 == 0 and computador / 2 == 1:
            jogador = False
            print('Perda do jogaro')
        elif jogador / 2 == 1 and computador / 2 == 0:
            jogador = False
            print('Perda do jogador')

print(f'O total de vitórias do jogador foram: {total_vitorias}')


#septuagésima nona tentativa com ajuda da IA e horas batendo cabeça querendo chorar e desistir de programar:


from random import randint


vitorias = 0

while True:
    computador = randint(0, 10)
    while True:
        escolha = (input('Escolha entre Par[P] ou Impar[I]: ')).strip().upper()
        if not escolha:
            print('Escolha entre P ou I')
            continue
        
        primeira = escolha[0]

        if primeira not in 'PI':
            print('Escolha entre P ou I')
            continue
        escolha = primeira
        break
        
    while True:
        try:
            print('Escolha um número: ')
            numero_jogador = int(input())
            break
        except ValueError:
            print('Escolha apenas números')
    resultado = (numero_jogador + computador) % 2
    tipo = 'PAR' if resultado == 0 else 'IMPAR'
    if (escolha == 'P' and resultado == 0) or (escolha == 'I' and resultado == 1):
        vitorias += 1
        print(f'Vitória do jogador! computador jogou {computador} jogador jogou {numero_jogador} resultado {tipo}')
    else:
        print(f'Derrota do jogador! computador jogou {computador} jogador jogou {numero_jogador} resultado {tipo}')
        break
    

print(f'O total de vitorias do jogador foram {vitorias}')


#OBS: Só não desisti ainda porque se não for pra fazer isso eu não sei o que vou fazer da minha vida, então prefiro ser um fracassado em uma coisa só do que ser um fracassado em tudo :)


#Como professor demonstrou:

from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')

    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')



