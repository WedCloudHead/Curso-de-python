#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: Mirin
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master 

#Como eu fiz:

atleta = int(input('Digite sua idade: '))
mirin = 9
infantil = 14
junior = 19
sênior = 25
master = 26

if atleta <= mirin:
    print(f'Sua idade é: {atleta}')
    print(f'Sua categoria é Mirin pois você não tem mais que {mirin} anos!')
elif atleta > mirin and atleta <= infantil:
    print(f'Sua idade é: {atleta}')
    print(f'Sua categoria é Infantil pois você tem mais que {mirin} anos e menos que {junior} anos!')
elif atleta > infantil and atleta <= junior:
    print(f'Sua idade é: {atleta}')
    print(f'Sua categoria é Junior pois você tem mais que {infantil} anos e menos de {sênior} anos!')
elif atleta > junior and atleta <= sênior:
    print(f'Sua idade é {atleta}')
    print(f'Sua categoria é Sênior pois você tem mais que {junior} anos e menos que {master} anos!')
else:
    print(f'Sua idade é: {atleta}')
    print(f'Sua categoria é Master pois você tem mais de {sênior} anos de idade!')

#Como professor demonstrou:

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')

#Anotações sobre esse problema:

#É importante notar o padrão sobre o encurtamento lógico do código, o quanto ambos andam juntos, nas linhas 42 a 51 feitas pelo professor ele usou uma comparação lógica entre as condições da qual se resume em, se a condição 1 não foi atendida, logicamente ela passa para o teste da condição dois e assim por diante, a ideia é que isso encurte totalmente o tamanho do código e resolva o problema com maior precisão e organização pois dessa forma não sera preciso ficar reinscrevendo várias vezes as mesmas condições para cada linha.

#Extra:

#Preciso pegar o costume de adicionar MÉTODOS EM MEUS CÓDIGOS, ALÉM DE SEREM 
#MAIS PRECISOS, SÃO TOTALMENTE ÚTEIS.


