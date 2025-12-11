#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais

#como eu fiz:

numero01 = int(input('Digite um numero inteiro qualquer: '))
numero02 = int(input('Digite outro numero inteiro qualquer:'))

if numero01 > numero02:
    print(f'O numero {numero01} é maior')
elif numero01 == numero02:
    print(f'O numero {numero01} é igual a o numero {numero02}')
else:
    print(f'O numero {numero02} é maior')


#Como professor demonstrou:

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior') 
else:
    print('Os dois valores são IGUAIS')

#Extra:

#Os dois programas resolvem o problema de forma excepcional! Mesmo tendo diferenças em suas ordens lógicas, nem todo código deve ser copia um do outro, desde que resolvam o problema! 
