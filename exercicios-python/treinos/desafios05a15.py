#Desafio04:

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))

#lembrando que independente do que for digitado (num ou str) python entendera tudo como str pois não fiz a declaração dizendo especificamente que tipo é.

a = input('Digite algo: ')
print('Só tem espaços? ', a.isspace())


#Nesse caso o python afirma como true caso so tenha espaço no input e false caso nao

a = input('Digite algo: ')
print('É um numero? ', a.isnumeric())

#Aqui ele mostra se o que você digitou é um numero ou nao

a = input('Digite algo: ')
print('É alfabetico? ', a.isalpha())

#Aqui é possivel ver se é alfabético, se tiver apenas letras sera true, caso contrario sera false

a = input('Digite algo: ')
print('É alfanumerico? ', a.isalnum())

#Este serve para identificar se tem letras e numeros juntos

a = input('Digite algo: ')
print('É maiusculas? ', a.isupper())
print('É minusculas? ', a.islower())

#Este é para saber se são maiusculas ou minusculas

a = input('Digite algo: ')
print('É capitalizada? ', a.istitle())

#Aqui serve para saber se toda string esta capitalizada, ou seja, com letra maiuscula no inicio.




#05faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero int: '))
sucessor = num + 1
antecessor = num - 1
print(f'O sucessor de {num} é {sucessor} e seu antecessor é {antecessor}')


#correção:

n = int(input('Digite um número: '))
print('Analizando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n - 1), (n - 2)))



#06crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um numero qualquer: '))
dobro = num * 2
triplo = num * 3
raizQuadrada = num ** (1/2) #raiz cubica seria: num ** (1/3)
print(f'O dobro de {num} é {dobro}, triplo é {triplo} e sua raiz quadrada é {raizQuadrada:.2f}')

#correção:
# A respostas estão muito parecidas 



#07desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02) / 2
print(f'A media do aluno é de {media}')


#correção:
# A respostas estão muito parecidas 




#08escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros


metro = float(input('Digite um valor de metro: '))
centimetros = metro * 100
mimilemtros = metro * 1000
print(f'O valor em centimetros de {metro} é {centimetros} e em milimetros é {mimilemtros}')

#correção:
# A respostas estão muito parecidas 



#09faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada


numero = int(input('Digite um numero inteiro qualquer para ver sua tabuada: '))
print('-' * 12)
print(f'{numero} x 1 = {numero * 1}, {numero} x 2 = {numero * 2}, {numero} x 3 = {numero * 3}\n, {numero} x 4 = {numero * 4}, {numero} x 5 = {numero * 5}, {numero} x 6 = {numero * 6}\n, {numero} x 7 = {numero * 7}, {numero} x 8 = {numero * 8}, {numero} x 1 = 9 {numero * 9}, {numero} x 10 = {numero * 10}')
print('-' * 12)

#10crie um programa que leia quanto tem na carteira e mostre quantos dolares ela pode comprar 
#(considere: uss1,00 = rs3,27)


carteira = float(input('Dê o valor de quanto tem na carteira: '))

dolar = float(3.27)
compra = dolar - carteira
print(f'Com R${carteira:.2f} real voce consegue comprar US{compra:.2f} dolar ')

#correção:

real = float(input('Dê o valor de quanto tem na carteira: R$'))
dolares = real / 3.27
print(f'Com R${real:.2f} voce pode comprar US{dolares:.2f}')



#11faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessario para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²


largura = float(input('Diga largura da parede: '))
altura = float(input('Diga a altura da parede: '))
area = altura * largura
tinta = area / 2
print(f'Para pintar essa parede serão gastos {tinta} de tinta')

#correção:
# A respostas estão muito parecidas 




#12faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto


produto = float(input('Digite o preço do produto: '))
desconto = produto * 5 / 100
valorfinal = produto - desconto
print(f'O preço do produto com 5% de desconto é de {valorfinal:.2f}')

#correção:
# A respostas estão muito parecidas 



#13faça um algoritmo que leia o salario e mostre seu novo salario, com 15% de aumento


salario = float(input('Digite o valor do salario: '))
aumento = salario * 15 / 100
aumentoreal = salario + aumento
print(f'Seu salario de {salario:.2f} ganha um aumento de 15% igual a {aumento} e vai para {aumentoreal:.2f} ')

#correção:
# A respostas estão muito parecidas 



#14faça um programa que converta °C em °F e mostre a conversão:


celsius = float(input('Digite uma temperatura em °C: '))
fahrenheit = ((9 * celsius) /5 ) + 32  
print(f'A conversão de {celsius} celsius para fahrenheit é de: {fahrenheit}')


#correção:
# A respostas estão muito parecidas 



#15escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por Km rodado.


kmPecorrido = float(input('Diga quantos km o carro percorreu: '))
dias = int(input('Diga a quantidade de dias o carro foi usado: '))
total = (dias * 60) + (kmPecorrido * 0.15)
print(f'O valor total a pagar pela utilização do carro é de: R${total:.2f}')


#correção:
# A respostas estão muito parecidas 



