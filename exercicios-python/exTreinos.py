#Exercicios de trigonometria:

#1)Aplicações diretas (básico)
#Calcular seno, cosseno e tangente de vários ângulos

#Peça ao usuário para digitar vários ângulos separados por vírgula
#(ex: 30, 45, 60, 90) e mostre uma tabela com seno, cosseno e tangente de cada um.


#import math
#usuario = float(input('Digite varios angulos separados por virgulas: '))

#tabela = [math.sin(usuario), math.cos(usuario), math.tan(usuario)]

#print(f'o seno, cosseno e a tangente de {usuario} é igual a {tabela}')



#2)Variáveis, Input e Operações

#1. Saudação Simples: Crie um programa que peça o nome do usuário e exiba a mensagem: "Olá, [Nome do Usuário]! Bem-vindo(a) ao Python."

#2. Soma de Números: Peça ao usuário que insira dois números inteiros e, em seguida, imprima a soma deles.

#3. Cálculo de Área: Peça ao usuário a largura e a altura de um retângulo e calcule sua área


#1)
nomeUsuario = str(input('Digite seu nome: ')).strip()

print('Olá {}, bem vindo(a) ao python '.format(nomeUsuario.capitalize()))


#2)
numero = int(input('Digite um numero: '))
numeoro2 = int(input('Digite outro numero: '))
soma = numero + numeoro2
print('O soma entre {} e {} é {} '.format(numero, numeoro2, soma))


#3)
largura = float(input('Digite o valor de uma largura: '))
altura = float(input('Digite o valor de uma altura: '))
area = largura * altura
print('A area desse retangulo é igual a {:.2f} '.format(area))



#3) Condicionais (if/else)

#4. Par ou Ímpar: Peça ao usuário um número inteiro e use uma estrutura condicional para determinar e exibir se o número é par ou ímpar.

#5. Classificação de Idade: Peça a idade do usuário. Se a idade for 18 ou mais, exiba "Você é maior de idade." Caso contrário, exiba "Você é menor de idade."

