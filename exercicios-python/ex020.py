#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


#Eu fiz assim:

 #import random 
 #João = 0
 #Pedro = 1
 #Maria = 2
 #Luís = 3
 #nomes = (João, Maria, Pedro, Luís)
 #ordem = random.random (nomes)

 #print('A ordem entre os alunos {}, {}, {}, {}, é essa {} '.format(João, Pedro, Maria, Luís, ordem))


#como professor demonstrou:

#1)
import random
n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo aluno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

#2)
from random import shuffle
n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo aluno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)



#Extra;

#muito parecido com exercicio anterior utilizando uma nova versão do modulo adicional, o shuffle 