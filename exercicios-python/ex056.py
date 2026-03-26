#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
#do programa, mostre:

#A média de idade do grupo.

#Qual é o nome do homem mais velho.

#Quantas mulheres têm menos de 20 anos.

#Como eu fiz a primeira resolução:


for pessoas in range(1, 5):
    str(input('Digite seu nome: '))
    int(input('Digite sua idade: '))
    float(input('Digite seu peso: '))
    str(input('Qual o seu sexo: '))
    


#Minha segunda resolução:


idade = 0
for c in range(1, 5, 1):
    candidatos = int(input('Digite sua idade: '))
    candidatos2 = input('Digite seu sexo: ')
    if not candidatos or not candidatos2:
        print('Você não digitou alguns dos valores anteriores!')
    else:
        try:
            candidatos00 = int(candidatos)
            candidatos02 = str(candidatos2)
            if candidatos02 in ('masculino'):
                idade = candidatos00
            elif candidatos02 in ('feminino'):
                idade = candidatos00 
            

        except ValueError:
            print('Digite os valores pedidos!')
print('Fim do programa!')


#Minha terceira resolução:



maior_idade = 0
menor_idade = 0
homens = str('masculino')
mulheres = str('feminino')
mulher = 0
homem = 0
for contador in range(1,5):
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            sexo = str(input('Digite seu sexo: '))
            break
        except ValueError:
            print('Digite corretamente os campos sugeridos!')
    
    if contador == 1:
        maior_idade = idade
        menor_idade = idade
        if sexo == homens:
            nome = str(input('Digite seu nome: ')) 
            homens = sexo
            if sexo == homens and idade > maior_idade:
                 homem = nome
        elif sexo == mulheres:
            mulheres = sexo
        if mulheres == sexo and idade < 20:
                mulher += 1
    else:
        if idade > maior_idade:  
            maior_idade = idade  
            if sexo == homens:
                nome = str(input('Digite seu nome: '))
                homens = sexo
                if sexo == homens and idade > maior_idade:
                 homem = nome
            elif sexo == mulheres:
                mulheres = sexo
            if mulheres == sexo and idade < 20:
                    mulher += 1
        if idade < menor_idade:
            menor_idade = idade
            if sexo == homens:
                nome = str(input('Digite seu nome: '))
                homens = sexo
                if sexo == homens and idade > maior_idade:
                 homem = nome
            elif sexo == mulheres:
                mulheres = sexo
            if mulheres == sexo and idade < 20:
                    mulher += 1
    
print(homens)
print(mulheres)
print(maior_idade)
print(menor_idade)
print(mulher)
print(nome)


#Quarta resolução:



média = 0
nome_homem_mais_velho = str()
mulher_menos_de_20 = 0
mulher = 0
maior_idade = 0
menor_idade = 0

for pessoas in range(1,5):
    while True:
        try:
            nome = str(input(f' {pessoas} Digite seu nome: '))
            idade = int(input(f'{pessoas} Digite sua idade: '))
            sexo = str(input(f'{pessoas} Digite seu sexo: '))
            break
        except ValueError:
            print('Digite corretamente os campos sugeridos!')
    
    if pessoas == 1:
        maior_idade = idade 
        menor_idade = idade
        if sexo == 'masculino':
            if idade > maior_idade:
                nome_homem_mais_velho = nome
    elif sexo == 'feminino':
        if idade < 20:
            mulher += 1
    else:
        if sexo == 'masculino' and idade > maior_idade:
            nome_homem_mais_velho = nome
        elif sexo == 'feminino' and idade < 20:
            mulher += 1

print(f'O total de mulheres com menos de 20 é {mulher}')
print(f'O nome do homem mais velho é {nome_homem_mais_velho}')



#Quinta resolução:



soma_de_idade = 0
mulheres_menos_20 = 0
homem_mais_velho = 0
nome_homem_mais_velho = ''

for pessoas in range(1,5):
    while True:
        try:
            nome = str(input(f'{pessoas} Digite seu nome: ')).strip().capitalize()
            idade = int(input(f'{pessoas} Digite sua idade: '))
            sexo = str(input(f'{pessoas} Digite seu sexo M/F: ')).strip().lower()
            break
        except ValueError:
            print('Digite corretamente os campos sugeridos!')

    soma_de_idade += idade

    if sexo == 'm':
        if idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem_mais_velho = nome
    
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1

media = soma_de_idade / pessoas

print(f'O nome do homem mais velho é {nome_homem_mais_velho}')
print(f'O total de mulheres com menos de 20 anos é de {mulheres_menos_20}')
print(f'A media de idade do grupo é de {media}')



#Como professor demonstrou:



somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----{p}ª Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1    

mediaidade = somaidade / 4

print(f'A média de idade do grupo é {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} com menos de 20 anos.')




#Sobre a primeira resolução:

#Ao me autoavaliar percebo meu avanço, minha primeira tentativa foi tão frustante que eu 
#não soube nem por onde começar, eu só consegui criar os inputs dentro do laço for.


#Sobre minha segunda resolução:

#Sobre essa resolução eu tentei abordar o problema de outra forma, tratando mudar os nomes
#das variáveis por exemplo, não é uma tática ruim porque faz você tentar abordar o mesmo 
#problema de um ponte de vista diferente, ainda não tinha me ajudado mas faz parte.


#Sobre a terceira e quarta resolução: 

#Aqui já é possivel perceber algum tipo de avanço, porém, na terceira resolução eu implementei
#tantas variáveis que acabei me perdendo na hora de validar ou de aplicar as condições.
#Na quarta resolução eu tentei reaproveitar a lógica da terceira porém tentando organizar 
#melhor o raciocínio e a estrutura, também não funcionou mas foi a base que eu precisava para
#finalmente concluir e resolver o problema na quinta resolução.


#Sobre a quinta resolução:

#A quinta resolução já começa com as variáveis corretas, não tem além do que é preciso, muito bom
#As condições para as variáveis também estão finalmente bem estruturadas atendendo certinho o que 
#precisa e faz sentido com o enuciado do problema.
#A media finalmente saiu certinha também, trabalhando fora do laço 
#e os prints finais também todos corretos.


#Sobre a resolução do professor:

#Não tem muito o que falar, resolve o problema perfeitamente, curiosidade interessante que a forma
#como ele resolveu o problema acabou no fim ficando muito parecido com a minha quinta resolução e 
#isso eu achei bem legal no fim.


