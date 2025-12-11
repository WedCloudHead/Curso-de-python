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


 

