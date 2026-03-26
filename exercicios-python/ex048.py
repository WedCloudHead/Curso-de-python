#Faça um programa que calcule a soma entre todos os números impares que são 
#multiplos de três e que se encontram no intervalo de 1 a 500.

#Como eu fiz:


print('Todos os numeros IMPARES DE 1 A 500: ')
for c in range(1 + 2, 500, 3 + 1): 
    print('>',c,'<')
    print(f'A soma entre {c} + {c} é igual à: {c + c}')
print('Fim')



#Como professor demonstrou:

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format (cont, soma))
print('')



#Sobre meu código:
#Meu programa nesse caso apresenta alguns vários erros, eu não soube
#interligar as condições no laço de repetição e de alguma forma eu tinha 
#achado que eu consegui fazer o contador pegar apenas os impares dos valores
#de 1 a 500, que de certa forma deu certo, o problema é que quando era pra 
#pegar os multiplos de 3 somente, acabou gerando os erros de conclusão.

#Sobre a aula do professor:
#É preciso pegar a explicação bem devagar pois tem vários conceitos aqui que 
#ensinam com maestria e corrige onde eu errei.

#Primeiro: linha 19 ele faz as combinações corretas, de 1 a 501 pulando de 2
#em 2 ou seja, já atendendo o primeiro pedaço do problema que é solicitar 
#somente os impares

#Segundo: linha 20 a condição if dentro do laço diz que só deve ser 
#considerado os numeros que divididos por tres o resto tem que dar 0 ou seja
#ja atendendo a outra parte do problema que é apenas os multiplos de 3

#Terceiro: linha 21 e 22 que dizem respeito tambem as linhas 17 e 18 são a 
#chave final do sucesso do programa  pois basicamente acontece o seguinte:

#soma: esse comando serve, como professor disse, como um acumulador ou seja, 
#ele recebe 0 mas quando posicionado abaixo do if o programa entende que no 
#final ele deve pegar todos os valores e somar com ele, então basicamente 
#como ele vale zero, o programa vai pegar e vai somar 3 + 9 + 0, 15 + 21 + 0,
#27 + 33 + 0... e assim por diante resolvendo mais um problema que é o da 
#soma final de todos os valores.

#cont: esse comando serve como um contador que quando posicionado dentro do 
#if ele basicamente pega a função de "cada numero impar que é multiplo de 3 
#que voce filtrar eu vou anotando aqui" como ele recebe zero o programa 
#entende que como ele é cont = cont + 1 cada vez que o programa somar um 
#grupo de multiplo de 3 ele adiciona como 1 ou seja, no final ele mostra 
#somente quantos numeros totais eram multiplos de 3.

#inclusive se o cont for um espaço para esquerda ele ja pega o totais de 
#numeros impares e para de pegar somente os multiplos de 3