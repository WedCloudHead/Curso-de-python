#Faça um programa que leia um número inteiro e diga se ele é ou não um número 
#primo.

#Como eu fiz:

usuario = int(input('Digite um numero inteiro qualquer: '))
if usuario % 2 == 1:
    print(f'O número: {usuario} é primo')
else:
    print(f'O número: {usuario} não é primo')




#Após voltar treinando e praticando esse foi meu segundo modo de refazer o desafio (03/03/2026):


usuario = int(input('Digite um valor qualquer: ')) 
não_é_primo = usuario // 2 == 0
não_é_primo2 = usuario == 0
não_é_primo3 = usuario // 2 == 5
não_é_primo4 = (usuario + usuario) // 3 == 0
for c in range(usuario):
    if usuario == não_é_primo:
        print('Não é primo!')
    elif usuario == não_é_primo2:
        print('Não é primo!')
    elif usuario == não_é_primo3:
        print('Não é primo!')
    elif usuario == não_é_primo4:
        print('Não é primo')
    else:
        print('É primo')
print('Fim do programa!')


# Terceira resolução do problema, após mais treinos: (5/03/26)

numero = int(input('Digite um numero: '))
contador = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        contador += 1
if contador == 2:
    print(f'O numero {numero} é primo!')
else:
    print(f'O numero {numero} não é primo')
print('Fim do programa!')



#Ao fim da resolução do professor virar a explicação desse meu novo método que usei para refazer o exercicio.


#Como o professor demonstrou:


num = int(input('Digite um número: ')) 
tot = 0 
if not num: #Wed
    print('Você não digitou valor algum!') #Wed
if num < 0: #Wed
    print('Digite valores positivos a partir de 0') #Wed
else: #Wed
    try: #Wed
        for c in range(1, num + 1): 
            if num % c == 0:
                print('\033[33m', end='')
                tot += 1
            else:
                print('\033[31m', end='')
            print(f'{c}', end='')
        print(f'\n\033[mO numero {num} foi divisivel {tot} vezes.')
        if tot == 2:
            print('E por isso ele é primo!')
        else:
           print('E por isso ele não é primo!')
    except ValueError: # Wed
     print('Tente de novo!') #Wed
print('Fim do programa!') #Wed



#1)Sobre a primeira resolução:
# Eu claramente não soube como fazer então eu simplismente fiz da forma que eu sabia
# que nem utilizou laço de repetição.

#2)Sobre a segunda resolução eu também não soube como fazer mas acredito que dê pra 
#dizer que houve um ganho em relação ao primeiro, tanto na tentativa da formação da
#da estrutura do código, quanto em utilizar o que se pede no enunciado.
#Porém nenhum dos meus dois códgido sanan de forma satisfatoria ou resolve o problema
#de fato!

#3)Sobre a terceira resolução:
#FINALMENTE!! Consegui pensar logicamente sobre o problema e finalmente resolve-lo
#É importante deixar claro que (APESAR DE ESTAR ESCRITO: PRIMEIRA RESOLUÇÃO, SEGUNDA 
#RESOLUÇÃO, ETC..) eu definitivamente não tentei apenas 3 vezes antes de conseguir.
#É porque eu só coloco no programa as conclusões finais resultantes das minhas várias tentativas
#esse problema mesmo levou dias e horas desses dias tentando até entender de fato.

#(Basicamente o numero (linha 39) vai ser o input digitado pelo usario, esse é o 
#numero que ele quer saber se é primo ou não. 
#Enquanto o contador (linha 40) vai servir como um banco que armazena quantas vezes
#o laço vai contar a condição do if acima (linha 42) ou seja, nesse sentido, como 
#eu escrevi: if numero % c == 0: se o numero dividido de forma inteira pelo c (laço) 
#que é do 1 até o número que o input escolheu for dividido e tiver resto zero, me mostre quantas
#vezes isso acontece no contador (linha 40). E eu sei que todo numero primo é dividido
#somente duas vezes, por 1 e por ele mesmo! ou seja na linha de baixo eu crio essas 
#condições que são: if contador == 2: (linha 44) se o contador contar só 2 numeros 
#exatos, significa que é primo! o print na (linha 45) é só pro usuario ver o numero
#escolhido por ele. E na penultima linha vem o else que é o contrario da primeira
#condição; ou seja se tiver mais de 2 contadores exatos, obrigatoriamente não pode
#ser primo.) 


#4)Sobre a resolução do professor:
#Toda a explicação dada na minha terceira resolução se encaixa na resolução do professor
#a diferença é que ele usou de artificios muito mais sofisticados para entregar uma 
#experiencia melhor ao usuario. 
#(IMPORTANTE AS LINHAS QUE CONTEM #Wed NA FRENTE NÃO ESTÃO NA RESOLUÇÃO DO PROFESSOR
#ESSAS LINHAS EU COLOQUEI, NÃO ALTERA EM NADA NA RESOLUÇÃO FINAL.)  