#Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor 

# como eu fiz (e falhei miseravelmente):

numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
numero3 = int(input('digite o terceiro numero: '))

if numero1 < numero2 and numero3:
    print('o primeiro numero é o menor')
else:
    numero2 < numero1 and numero3
    print('o segundo numero é o menor')
    

numero01 = int(input('digite o primeiro numero: '))
numero02 = int(input('digite o segundo numero: '))
numero03 = int(input('digite o terceiro numero: '))

if numero01 < numero02 < numero03:
    print('1 é menor')
else:
    print('1 é menor')
if numero01 < numero02 > numero03:
    print('1 é menor')
else:
    print('1 é menor')
if numero02 < numero01 < numero03:
    print('o 2 é menor')
else:
    print('2 é menor')
if numero02 < numero01 > numero03:
    print('o 2 é menor')
else:
    print('2 é menor')
if numero03 < numero01 < numero02:
    print('0 3 é menor')
else:
    print('3 é menor')
if numero03 < numero01 > numero02:
    print('o 3 é menor')
else:
    print('3 é menor')

#Como professor demonstrou:

a = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
c = int(input('digite o terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print(f'O menor numero é o {menor}')
print('a cima esta verificado qual é o menor!')
maior = b
if a > b and b > c:
    maior = a
if c > a and c > b:
    maior = c
print(f'O maior numero é o {maior}')
print('a cima esta verificado qual é o maior!')

#Sobre esse exercicio não tem muito o que dizer, foi um erro de logica mesmo, eu tentei entender a logica do problema de diversas vezes, mesmo tendo deixado no resultado final somente duas tentativas diferentes, no exemplo de cima teve elementos que seriam uteis no segundo exemplo e vise e versa, porem ambas não sanaram o problema que era isolar somente o menor e o maior numero e ter eles como resultados finais. Inclusive nos dois primeiros problemas eu so tenho a metade da tentativa da resolução porque eu sabia que se eu acha-se e isola-se o menor numero, era so apĺicar igualmente para achar o maior mas como demonstrado eu não consegui resolver nem a primeira parte do problema. Lado bom é que depois da resolução ficou claro pra mim agora como abordar problemas desse tipo.


