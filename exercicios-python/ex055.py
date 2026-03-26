#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.


#Como eu fiz:

for peso in range(1, 6):
    usuarios = float(input('Digite seu peso: '))
    
print()


#Segunda resolução:


peso = float(300)
for c in range(1, 6, 1):
    pessoas = float(input(('Digite seu peso: ')))
    if not pessoas:
        print('Você não digitou valor algum!')
    if pessoas < 0:
        print('Você precisa colocar pesos positivos!')
    else:
        try:
            pessoa = float(pessoas)
        except ValueError:
            print('Digite somente valores numericos!')
print('A comparação entre os pesos são: ')


print('-----')
if pessoa < 300:
    print(f'O maior peso entre todos é: {pessoa}')
print('Fim do contador!')


#Terceira resolução:



maior_peso = 0
menor_peso = 0
mais_pesado = float()
mais_leve = float()
for p in range(1,6):
    while True:
        try:
            pessoa = float(input(f'Digite o valor do peso da {p}° pessoa: '))
            break
        except ValueError:
            print('Erro! Digite apenas números para ler o peso!.')

    print(pessoa)
    maior_peso += 1
    print(pessoa)
    menor_peso += 1

    if pessoa > pessoa:
        pessoa = mais_pesado
    elif pessoa < pessoa:
        pessoa = mais_leve
    else:
        pessoa == pessoa
print(f'Pessoa mais pesada tem {mais_pesado}kg')
print(f'Pesoa mais leve tem {mais_leve}kg')



#Quarta resolução:


maior_peso = 0
menor_peso = 0

for p in range(1,6):
    while True:
        try:
            pessoa = float(input(f'Digite o valor do peso da {p}° pessoa: '))
            break
        except ValueError:
            print('Erro! Digite apenas números para ler o peso!.')

    if p == 1:
        maior_peso = pessoa
        menor_peso = pessoa
    else:
        if pessoa > maior_peso:
            maior_peso = pessoa
        if pessoa < menor_peso:
            menor_peso = pessoa
print(f'Pessoa mais pesada tem {maior_peso}kg')
print(f'Pesoa mais leve tem {menor_peso}kg')



#Resolução do professor:


maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')




#Sobre a primeira resolução:
#Sim na minha primeira resolução eu não soube nem como iria deixar o print e desisti logo de 
#cara :)


#Sobre a segunda resolução:
#Eu pensei em fazer algo como o professor disse que algumas pessoas fazem e alguns professores ensinam 
#E ainda sim eu não tinha uma ideia muito desenvolvida sobre como eu iria desenvolver melhor a estrutura
#do código, a partir da (linha 26 até 33) foi puro improviso.


#Sobre a terceira resolução:
#Dá pra se dizer que da (linha 40 até 64) teve uma estrutura decente com as variáveis fazendo um pouco mais 
#de sentido, as (linhas 42 e 43) na minha cabeça já começou a surgir a ideia de que deveria ter uma variável
#que guardasse um valor vazio para que depois esse valor vazio assumisse o novo valor das condições do 
#programa; a ideia em si não é ruim mas a execução em si está bem quebravel.
#(As linhas 44 a 50) me deixou bem orgulho porque ali eu tratei o problema de erro no programa com while
#e true fazendo o programa criar um loop infinito enquanto a condição dada não for atendida e mais 
#interessante ainda foi que eu coloquei o while dentro do for fazendo com que o ele valha enquanto o laço
#de repetição estiver valendo também.
#Porém da (linha 57 a 62) não faz sentido pois eu estou lendo nessas linhas as variáveis mais_pesado e 
#mais_leve com pessoas sendo que essas variáveis valem 0.0 e ainda sim não seria daquela forma o jeito certo
#de comparar as variáveis; Os prints finais também acabam que não recebem valores pois as variáveis que eles
#estão lendo valhem 0.0
#Infelizmente ou felizmente essa terceira resolução ainda não resolve o problema.


#Sobre a quarta resolução:
#Aqui sim, uma mudança real acontece, (linhas 71 e 72) com os contadores certinhos esperando para serem 
#adicionados ao programa, das (linhas 74 a 80) for com while tratando controle de defeito corretamente e 
#limpo, e agora sim das (linhas 82 a 89) as condições pegando certinho os contadores, fazendo com que o 
#python leia se não for a primeira volta do laço ja compare os novos valores com o primeiro, nesse sentido
# na (linha 82) o comando: if p == 1: ou seja se for primeiro laço guarde: maior_peso = pessoa e menor_peso =
#pessoa se não for a primeira volta do laço, somente ignore esse bloco e passe para as proximas condições, 
#nesse sentido toda vez ou em cada volta do laço que ele lê o peso, se for maior que anterior, ele assume a 
#nova posição e o mesmo com o menor peso e assim ele faz até o último laço, até o último input.


#Sobre a resolução do professor:
#Básicamente a minha quarta resolução e a resolução do professor são práticamente iguais, tirando 
#tratamento de erro que adicionei no meu programa.
#Uma curiosidade interessante também foi que o professor deu o nome ao for dele de p assim como eu fiz no meu
#programa, isso com certeza sem eu saber pois minhas resoluções foram feitas antes da aula de 
#explicação do professor.


