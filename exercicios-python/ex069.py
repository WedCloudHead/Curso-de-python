#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos que 20 anos.



#Como eu fiz:




mais_18 = 0
homens = 0
mulheres_menos20 = 0



while True:
    while True:
        try:
            entrada = input('Digite sua idade: ')
            if not entrada:
                print('O campo não pode estar vazio')
                continue
            idade = int(entrada)
            if idade <= 0 or idade > 120:
                print('Digite apenas idades acima de 0 ou menor que 120 anos')
                continue
            if idade > 18:
                mais_18 += 1

            break
        except ValueError:
            print('Digite apenas números')

    while True:
        try:
            sexo = input('Digite seu sexo [M/F]: ').strip().upper()
            if not sexo:
                print('O campo não pode estar vazio')
                continue
            if not sexo.isalpha():
                print('Digite apenas letras')
                continue
            primeira = sexo[0]
            if primeira not in 'MF':
                print('Escolha entre M(masculino) ou F(feminino)')
                continue
            sexo = primeira

            if sexo == 'M':
                homens += 1
            if sexo == 'F' and idade <20:
                mulheres_menos20 += 1

            break
        except IndexError:
            print('Digite conforme sugerido')


    while True:
        print('Deseja continuar [S/N] ? ')
        escolha = input().strip().upper()
        if not escolha:
            print('O campo não pode estar vazio')
            continue
        usuario = escolha[0]
        if usuario not in 'SN':
            print('Digite apenas Sim ou não')
            continue
            
        break

    if usuario == 'N':
        break
    '''else:
        usuario = entrada  (Essa linha 86 e 87 é irrelevante porém eu deixo para ter um parâmetro)'''

print(f'Resultado dos Cadastros: ')
print(f'Pessoas com mais de 18 anos: {mais_18}')
print(f'Quantidade de homens: {homens}')
print(f'Ao todo, {mulheres_menos20} mulheres cadastradas tem menos de 20 anos')

print('Fim do programa')


#Como o professor demonstrou:

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    print(f'Total de pessoas com mais de 18 anos: {tot18}')
    print(f'Ao todo temos {totH} homens cadastrados')
    print(f'E temos {totM20} mulheres com menos de 20 anos')
    