#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

#ex: digite o numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#como eu fiz:

numero = '2987'

print('Nesse numero tem:', (numero[3]), 'unidades')

print('Nesse numero tem:',(numero[2]), 'dezenas')

print('Nesse numero tem:',(numero[1]), 'centenas')

print('Nesse numero tem:',(numero[0]), 'milhar')

#dessa forma que eu desenvolvi que acredito ser a forma que qualquer pessoa pense logo de cara, não resolve totalmente o problema pois do jeito que esta, o programa é capaz apenas de identificar e nomear 4 digitos da ordem numerica, deixando uma brecha clara e rigorosa.


#Como professor demonstrou:

numero = int(input('Digite uma ordem numerica de quantos digitos quiser: '))

uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print('Analizando o numero {} '.format(numero))
print(' Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {} '.format(uni, dez, cen, mil))


#Extra:

#importante notar que a forma mais correta e otimisavel de se resolver esse problema seria utilizando funções e variaveis porem ainda não aprendemos isso ainda entao o professor resolveu o problema de uma forma matematica, nada mais que contas simples de divisão inteira (//) mais o resto da divisão (%) como todos estão por 10 sempre vai ser a divisão inteira considerando "10 por cento" desse valor da divisão inteira, sendo impossivel errar assim.


#treinando mais um pouco:
num = int(input('Digitando um numero qualquer: '))
unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10 
milhares = num // 1000 % 10
centena_de_mil = num // 100000 % 10

print(f'{unidades}, {dezenas}, {centenas}, {milhares}, {centena_de_mil}')