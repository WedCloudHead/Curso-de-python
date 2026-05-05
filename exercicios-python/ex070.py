#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos cutam mais de R$1000.
#C) qual nome do produto mais barato.





    
#Primeira tentativa:


total_gasto = 0
produto_mais_1000 = []
nome_produto_mais_barato = []
listas_produtos_baratos = []
preços = []



while True:    
    produto = input('Digite o nome do produto: ').strip()
    if not produto:
        print('Preencha o campo corretamente')
        continue
    if not produto.isalpha():
        print('Digite apenas letras')
        continue
    while True:
        try: 
            preço = float(input('Digite o preço do produto: '))
        except ValueError:
            print('Digite apenas números')
            continue
        total_gasto += preço
        if preço > 1000:
            produto_mais_1000.append(preço)
        break
        
    while True:    
        primeiro = input('Deseja continuar? (S) ou (N)').strip().upper()
        if not primeiro:
            print('Escreva apenas S ou N')
            continue
        usuario = primeiro[0]
        if usuario not in 'SN':
            print('Digite apenas S(sim) ou N(não)')
            continue
        if usuario == 'S':
            usuario = produto
        elif usuario == 'N':
            break
        
    break

print('Fim do programa')







#Segunda tentativa:

usuario = 'S'

while usuario == 'S':
    while True:    
        produto = input('Digite o nome do produto: ').strip()
        if not produto:
            print('Preencha o campo corretamente')
            continue
        if not produto.isalpha():
            print('Digite apenas letras')
            continue
        break
    while True:
        try: 
            preço = float(input('Digite o preço do produto: '))
        except ValueError:
            print('Digite apenas números')
            continue
        total_gasto += preço
        if preço > 1000:
            produto_mais_1000.append(preço)
        break
    while True:    
        primeiro = input('Deseja continuar? (S) ou (N)').strip().upper()
        if not primeiro:
            print('Escreva apenas S ou N')
            continue
        usuario = primeiro[0]
        if usuario not in 'SN':
            print('Digite apenas S(sim) ou N(não)')
            continue
        if usuario == 'S':
            usuario = produto
        elif usuario == 'N':
            break
        
print('Fim do programa')
        



#Terceira tentativa:


total_gasto = qtd_produto_mais_1000 = 0
nome_produto_mais_barato = ''
menor_preço = None



print('--'*10, 'LOJÂO DO WEDÃO', '--'*10)


while True:
    while True:    
        produto = input('Digite o nome do produto: ').strip()
        if not produto:
            print('Preencha o campo corretamente')
            continue
        
        break
    while True:
        try:
            valor = input('Digite o preço do produto: ')
            preço = float(valor)
        except ValueError:
            print('Digite apenas números')
            continue
        total_gasto += preço
        if preço > 1000:
            qtd_produto_mais_1000 += 1

        break
    
    if menor_preço == None: #mais usado dessa forma: if menor preço is None    (esse is no caso faz mais sentido)
        menor_preço = preço
        nome_produto_mais_barato = produto
    else:
        if preço < menor_preço:
            menor_preço = preço
            nome_produto_mais_barato = produto
        
    primeiro = input('Deseja continuar? (S) ou (N)').strip().upper()
    if not primeiro:
        print('O campo não pode estar vazio, escreva apenas S ou N')
        continue
    usuario = primeiro[0]
    if usuario not in 'SN':
        print('Esolha entre S(sim) ou N(não)')
        continue
    if usuario == 'N': 
        break
    

   

    

print(f'Ao todo {qtd_produto_mais_1000} produtos custam mais de R$1000')
print(f'O produto mais barato é {nome_produto_mais_barato} custando R${menor_preço:.2f}')
print(f'O total de gastos nas compras foram {total_gasto}')

print('Fim do programa')


#Como profesor demonstrou: 

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos mais de R$!000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
