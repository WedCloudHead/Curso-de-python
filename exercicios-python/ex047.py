#Crie um programa que mostre na tela todos os números pares que estão no 
#intervalo entre 1 e 50.

#Como eu fiz:

for c in range(1 + 1, 50 + 1, 2):
    print('Todos os números pares: ', c)
print('Fim!')


#Como professor demonstrou:

for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')

#Esse formato a partir da linha 13 é apenas pra demonstrar que cada ponto 
#representa quantas vezes o laço de repetição está sendo feito antes de fato
#entegar os numeros, nesse caso duas "laçadas" e isso é de certa forma 
#corrigivel, como demonstrado no código abaixo.

for n in range(2, 51, 2):
    print('.', end='')
    print(n, end=' ')
print('Acabou')

#Basicamente a diferença é que o trabalho no processador é reduzido pela 
#metade, em programas curtos não faz diferença talvez seja interessante 
#lembrar disso para programas grandes e mais complexos


#Anotação:
#As linhas 14 e 25 com esse ponto são apenas pra demonstração como explicado 
#acima, não fazem diferença pro programa final.