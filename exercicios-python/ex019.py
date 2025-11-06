#um professor que sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.


#Eu fiz assim: :(

   #import random
   #sorteio = random.random(Ana, Beto, Carla, Maria)
   #Ana = 1
   #Beto = 2
   #Carla = 3
   #Maria = 4
   #print('e o escolheido foi {} '.format(Ana, Beto, #Carla, Maria))


#como professor demonstrou: 

#1)
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {} '.format(escolhido))


#2)
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)
print('O aluno escolhido foi: {} '.format(escolhido))



#Importante:

#lembrando que a declaração str nas linhas 18 a 22 não sao obrigatorias; na linha 24 é mostrado o modulo random.choice que foi importado lembrando que esse choice é um dos diversos modulos adicionais que aparecem ao precionar ctrl + space depois de digitar random., cada problema envolvendo random usara um modulo adicional diferente(possivelmente) é interessante pesquisar rapidamente qual modulo adicional sera o necessario para cada problema.