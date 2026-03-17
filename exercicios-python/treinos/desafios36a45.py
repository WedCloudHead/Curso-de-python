#36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario ou então o empréstimo será negado.

casa = float(input('Diga o valor da casa R$: '))
comprador = float(input('Diga o sálario atual R$: '))
prestação = int(input('Diga em quantas prestações vai pagar: '))
comprador = comprador * 30 / 100

if casa / (prestação * 12) > comprador:
    print('Você não tem limite de emprestimo bancário para comprar esse imóvel!')
else:
    casa / (prestação * 12) <= comprador
    print('Você tem limite bancário para comprar esse imóvel!')
print('Fim da simulação!')

#Correção, ficou correto porém está diferente do jeito que o professor fez.




#37 escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# -1 para binário
# -2 para octal
# -3 para hexadecimal


num = int(input('Diga um número inteiro qualquer para ver sua conversão: '))
print('''   
            Digite [ 0 ] para converter para Binário:
            Digite [ 1 ] para converter para Octal:  
            Digite [ 2 ] para converter para Hexadecimal:  
      ''')
opção = int(input('Sua opção: '))
if opção not in (0, 1, 2):
    print('Apenas os valores 0, 1, 2 são permitidos')
else:
    if opção == 0:
        print(f'O numero {num} convertido para Bínario é igual a {bin (num)}')
    elif opção == 1:
        print(f'O numero {num} convertido para Octal é igual a {oct (num)}')
    elif opção == 2:
        print(f'O numero {num} convertido para Hexadecimal é igual a {hex (num)}')
    else:
        print('Nenhum Numero foi escolhido :(')
print('Fim! tente de novo! ')


#Correção: ficou muito parecido com o do professor, obs: a linha 46 e 47 não estão funcionando pois não é tão facil assim fazer o rograma ler um valor inexistente nos exercicios abaixo ja mostro como se faz isso, primeiro é preciso fazer o programa ler o input como se fosse str e depois transforma ele me num.


#38 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais


num0 = int(input('Digite um numero qualquer inteiro: '))
num01 = int(input('Digite um outro numero qualquer inteiro: '))
if num0 > num01:
    print(f'O numero {num0} é maior que o numero {num01}')
elif num0 < num01:
    print(f'O numero {num01} é maior que o numero {num0}')
else:
    print('Não existe valor maior, ambos são iguais!')



#Correção: Está muito parecido com o a correção do professor!





#39 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# -Se ele ainda vai se alistar ao serviço militar
# -Se é a hora de se alistar
# -Se já passou do tempo do alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
espera = input('Digite sua data de nascimento: ').strip()
ano = date.today().year

if not espera:
    print('Você não digitou valor algum! Tente de novo.')
else:
    try:
        pessoa = int(espera)

        if ano - pessoa < 18:
            print(f'Você ainda é muito jovem para se alistar! faltam {ano - pessoa - 18} anos!')
        elif ano - pessoa == 18:
            print('Você já tem 18 anos! Está na hora de se alistar.') 
        elif ano - pessoa > 18:
            print(f'Já passou da hora de se alistar! Era para ter se alistado a {ano - pessoa - 18} anos atras.')
    except ValueError:
        print('Digite apenas numeros válidos!')
print('Fim do programa!')






#40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# -Média abaixo de 5.0: Reprovado
# -Média entre 5.0 e 6.9: Recuperação
# -Média de 7.0 ou superior: Aprovado



entrada01 = input('Diga o valor da sua primeira nota: ').strip()
entrada02 = input('Diga o valor da sua segunda nota: ').strip()
if not entrada01 or not entrada02:
    print('Você não digitou valor algum! Tente de novo')
else:
    try:
        nota01 = float(entrada01)
        nota02 = float(entrada02)
        
        if nota01 > 10 or nota02 > 10 or nota01 < 0 or nota02 < 0:
            print('Os valores maximos permitidos são de no minimo 0 ou de no maximo 10')
        else:
            media = (nota01 + nota02) / 2

            if media < 5.0:
                print(f'Não atingiu a média de 5.0! sua média foi {media:.2f}')
            elif media >= 7.0:
                print(f'Ultrapassou a média de 5.0! sua nota foi {media:.2f}')
            else:
                print(f'Está dentro da média de 5.0 a 6.9 e está de recuperação')
    except ValueError:
        print('Digite apenas números válidos!')
print('Fim do programa!')


#Correção: O programa funciona sem falhas, só não está exatamente identico ao do professor pois eu encurtei a logica, simplificando as condições.




#41 A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master 


emput = input('Diga sua idade: ').strip()
if not emput:
    print('Você não digitou valor algum!')
else:
    try:
        idade = int(emput)

        if idade < 0:
            print('Só é permitido valor acima de 0 anos!')
        else:
            if idade <= 9:
                print(f'Você tem {idade} e está na categoria Mirim')
            elif idade >= 10 and idade <= 14:
                print(f'Você tem {idade} e está na categoria Infantil')
            elif idade >= 15 and idade <= 19:
                print(f'Você tem {idade} e está na categoria Junior')
            elif idade >= 20 and idade <= 25:
                print(f'Você tem {idade} e está na categoria Sênior')
            elif idade >= 26:
                print(f'Você tem {idade} e está na categoria Master')
    except ValueError:
        print('Digite apenas números validos!')
print('Fim do programa!')



#Correção: A diferença dos dois programas é que um mostra as condições caso o usuario responda a idade que tem e o outro caso o usuario responda em que ano nasceu. Ambos os programas estão funcionando 100%


from datetime import date
atualmente = date.today().year
nascimento = input('Ano de nascimento: ')
if not nascimento:
    print('Você não digitou valor algum!')
else:
    try:
        nascido = int(nascimento)
        idade = atualmente - nascido
        if nascido > atualmente or nascido <= 1900:
            print('Você não pode ter nascido no ano que vem e nem ter mais de 120 anos e ainda estar vivo!')
        else:
            print(f'O atleta tem {idade} anos')
            if idade <= 9:
                print('Classificação: Mirim')
            elif idade <= 14:
                print('Classificação Infantil')
            elif idade <= 19:
                print('Classificação Junior')
            elif idade <25:
                print('Classificação Sênior')
            else:
                print('Classificação Master')
    except ValueError:
        print('Digite apenas valores numericos!')
print('Fim do programa')




#42 Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais 
# Escaleno: todos os lados diferentes


entrada1 = input('Diga o valor da primeira reta:').strip()
entrada2 = input('Diga o valor da segunda reta:').strip() 
entrada3 = input('Diga o valor da terceira reta:').strip()
if not entrada1 or not entrada2 or not entrada3:
    print('Você não digitou os 3 valores completamente!')
else:
    try:
        reta1 = int(entrada1)
        reta2 = int(entrada2)
        reta3 = int(entrada3)

        if reta1 < 0 or reta2 < 0 or reta3 < 0:
            print('São permitidos somentes valores positivos!')
        else:
            if reta1 == reta2 == reta3:
                print('É um triangulo Equilátero')
            elif reta1 == reta2 > reta3 or reta1 == reta2 < reta3 or reta1 == reta3 > reta2 or reta1 == reta3 < reta2 or reta2 == reta3 > reta1 or reta2 == reta3 < reta1:
                print('É um triangulo Isósceles')
            elif reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
                print('É um triangulo Escaleno')
            else:
                print('Dado os valores a cima não é possivel formar um triangulo!')
    except ValueError:
        print('Digite apenas valores numéricos!')
print('Fim do programa!')


#Correção: Poderia ter ficado mais compacto, principalmente a linha 240.




#43 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5:   Abaixo do peso

# Entre 18.5 e 25:  Peso ideal 

# 25 a 30:          Sobrepeso

# 30 até 40:        Obesidade

# Acima de 40:      Obesidade morbida 


peso = input('Digite seu peso Kg: ').strip()
altura = input('Digite sua altura m: ').strip()

if not peso or not altura:
    print('Você não digitou algum dos valores!')
else:
    try:
        pesos = float(peso)
        alturas = float(altura)
        imc = pesos / (alturas ** 2)
        if pesos < 0 or alturas < 0:
            print('Somente numeros positivos serão aceitos!')
        else:
            if imc < 18.5:
                print(f'Abaixo do peso! Seu IMC é de {imc:.2f}')
            elif 18.5 <= imc < 25:
                print(f'Peso ideal! Seu IMC é de {imc:.2f}')
            elif 25 <= imc < 30:
                print(f'Sobrepeso! Seu IMC é de {imc:.2f}')
            elif 30 <= imc < 40:
                print(f'Obesidade! Seu IMC é de {imc:.2f}')
            elif imc >= 40:
                print(f'Obesidade morbida! Seu IMC é de {imc:.2f}')
    except ValueError:
        print('Digite apenas valores numericos')
print('Fim do programa IMC')







#44 Elabore um programa que calcule um valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros


teclado00 = input('Digite o preço do produto R$: ').strip()
if not teclado00:
    print('Você não digitou valor algum!')
else: 
    try:
        print('{:=^40}'.format('Lojas Torres')) 
        teclado01 = input('''
                  Escolha a forma de pagamento: 
                  [ 1 ] À vista! (10 por cento de desconto)
                  [ 2 ] À vista no cartão! (5 por cento de desconto)
                  [ 3 ] Em 2x no cartão! (preço normal)
                  [ 4 ] Em 3x ou mais no cartão! (20 por cento de juros)
                  ''')
        produto = float(teclado00)
        escolha = int(teclado01)
        if escolha not in (1, 2, 3, 4):
            print('Apenas as opções 1 2 3 e 4 serão permitidas!')
        else:
            if escolha == 1:
                print(f'O valor do produto {produto:.2f} pago a vista adquiri 10 por cento de desconto, ficando {produto - (produto * 10 / 100)}')
            elif escolha == 2:
                print(f'O valor do produto {produto:.2f} pago a vista no cartao adquiri 5 por cento de desconto, ficando {produto - (produto * 5 / 100)} ficando 2x de {produto - (produto * 5 / 100)}')
            elif escolha == 3:
                print(f'O valor do prosduto {produto:.2f} pago em 2x no cartão sai pelo valor liquido do produto {produto:.2f}')
            elif escolha == 4:
                print('De quantas vezes deseja dividir? ')
                opçao = input('''
                         [3x] [4x] 
                         [5x] [6x] 
                         [7x] [8x] 
                         [9x] [10x]
                            ''').strip()          
                if not opçao:
                            print('Você não digitou valor algum!')
                else:
                    try:
                        escolhas = int(opçao)
                        if escolhas not in (3, 4, 5, 6, 7, 8, 9, 10):
                            print('Apenas as opções 3, 4, 5, 6, 7, 8, 9, 10 serão consideradas!')
                        else:  
                            escolhas == 3
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 3x')
                        if escolhas == 4:
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 4x')
                        elif escolhas == 5:
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 5x')
                        elif escolhas == 6:
                                    print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 6x')
                        elif escolhas == 7:
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 7x')
                        elif escolhas == 8:
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 8x')
                        elif escolhas == 9:
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 9x')
                        elif escolhas == 10:
                            print(f'O valor do produto {produto:.2f} pago em 3x ou mais no cartão sofre um juros de 20 por cento, ficando {produto + (produto * 20 / 100)} dividido de 10x')
                    except ValueError:
                                print('Digite apenas valores numéricos')
    except ValueError:
        print('Digite apenas o valor numerico!')
print('Fim do programa!')




#45 Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
print('{:=^40}'.format('Jogo do Jokenpô'))
print('O computador jogara contra você, faça sua escolha!')

pedra = int(1)
papel = int(2)
tesoura = int(3)
lista = [pedra, papel, tesoura]
tec = input('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA 
''')

if not tec:
    print('Você não digitou valor algum!')
else:
    try:
        comp = choice(lista)
        jogador = int(tec)
        if jogador not in (1, 2, 3):
            print('Você precisa escolher entre as alternativas 1, 2 e 3!')
        else:
            print('JO KEN PÔ:')
            sleep(2)    
            if jogador == 1 and comp == 2:
                print(f'Vitoria do computador!! Sua escolha {jogador}: PEDRA VS Computador {comp}: PAPEL')
            elif jogador == 1 and comp == 3:
                print(f'Vitoria do jogador!! Sua escolha {jogador}: PEDRA VS Computador {comp}: TESOURA')
            elif jogador == 2 and comp == 1:
                print(f'Vitoria do jogador!! Sua escolha {jogador}: PAPEL VS Computador {comp}: PEDRA')
            elif jogador == 2 and comp == 3:
                print(f'Vitoria do computador!! Sua escolha {jogador}: PAPEL VS Computador {comp}: TESOURA')
            elif jogador == 3 and comp ==1:
                print(f'Vitoria do computador!! Sua escolha {jogador}: TESOURA VS Computador {comp}: PEDRA')
            elif jogador == 3 and comp == 2:
                print(f'Vitoria do jogador!! Sua escolha {jogador}: TESOURA VS Computador {comp}: PAPEL')
            else:
                if jogador == 1 and comp == 1:
                 print(f'Houve um empate!! Sua escolha {jogador}: PEDRA VS Computador {comp}: PEDRA')
                elif jogador == 2 and comp == 2:
                    print(f'Houve um empate!! Sua escolha {jogador}: PAPEL VS Computador {comp}: PAPEL')
                elif jogador == 3 and comp == 3:
                    print(f'Houve um empate!! Sua escolha {jogador}: TESOURA VS Computador {comp}: TESOURA')

    except ValueError:
        print('Você precisa digitar um valor numerico')
print('fIM DO JOGO!')
