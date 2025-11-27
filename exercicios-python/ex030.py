#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

#Como eu "fiz"

jogador = int(input('escolha um numero inteiro e o programa te dira se ele é par ou impar: '))

par = int(0 and 2 and 4 and 6 and 8)
impar = int(1 and 3 and 5 and 7 and 9)

if jogador == par:
    print('seu numero escolhido é par')
else:
    print('Seu numero escolhido é impar')


#Como professor demonstrou:

numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2

if resultado == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')


#Extra:

#É um exercicio de execussão simples porem eu pequei na matematica, por não saber que o resto de qualquer numero par divido por 2 sempre é 0 e o resto de qualquer numero impar divido por 2 sempre é 1, me fez não saber como montar a estrutura logica para o funcionamento do programa.