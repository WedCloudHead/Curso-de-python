#16crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.


from math import ceil
num = float(input('Digite um numero real qualquer: '))
inteiro = ceil(num)
print(f'O numero inteiro de {num} é {inteiro}')



#17faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.


from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('DIgite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O comprimento da hipotenusa é de: {hi:.2f}')




#18faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import sin, cos, tan, radians
angulo = float(input('Digite um angulo qualquer: '))
tangente = tan(radians(angulo))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
print('-' * 12)
print(f'A tangente de {angulo} é de {tangente:.2f}, o seno de {angulo} é de {seno:.2f}, o cosseno de {angulo} é de {cosseno:.2f}')
print('-' * 12)

#19um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
from time import sleep
al1 = str('jorge')
al2 = str('pedro')
al3 = str('maria')
al4 = str('carla')
lista = [al1, al2, al3, al4]
escolha = choice(lista)
print('-' * 12)
sleep(3)
print(f'Dentre os quatro alunos, o sorteado é: {escolha}')
print('-' * 12)


#20o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


from random import shuffle
from time import sleep
al1 = str('jorge')
al2 = str('pedro')
al3 = str('maria')
al4 = str('carla')
lista = [al1, al2, al3, al4]
escolha = shuffle(lista)
print('-' * 12)
sleep(3)
print(f'A ordem da lista sorteada entre os alunos são: {lista}')
print('-' * 12)

