#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: Mirin
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master 

#Como eu fiz:

atleta = int(input('Digite sua idade: '))
mirin = 9
infantil = 14
junior = 19
sênior = 20
master = 21

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

