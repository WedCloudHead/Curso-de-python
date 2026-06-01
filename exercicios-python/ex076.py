#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços organizando os dados de forma tabular.



#Primeira tentativa:


produto_preço = ('Arroz' , 'R$' , 23.00 , 'Feijão', 'R$' , 13.00 , 'Coador', 'R$' , 6.90 , 'Mel', 'R$' , 10.00 , 'Café', 'R$' , 24.00)



print('---' * 20)
print('{:^60}'. format('TABELA DE PREÇOS'))
print('---' * 20)

print('===' * 20)
print(produto_preço[0:1],   '-' * 37, produto_preço[1:3])
print('===' * 20)
print(produto_preço[3:4],  '--' * 18, produto_preço[4:6])
print('===' * 20)
print(produto_preço[6:7],  '--' * 18, produto_preço[7:9])
print('===' * 20)
print(produto_preço[9:10],  '-' * 39, produto_preço[10:12])
print('===' * 20)
print(produto_preço[12:13], '-' * 38, produto_preço[13:15])
print('===' * 20)



#Segunda tentativa: 
produto_preço = ('Arroz', 23.00 , 'Feijão', 13.00 , 'Coador', 6.90 , 'Mel', 10.00 , 'Café', 24.00) 
for p in produto_preço[0:11:2]: 
    print(p) 

for i in produto_preço[1:11:2]: 
    print(i)




#Terceira tentativa:

produto_preço = ('Arroz', 23.00 , 'Feijão', 13.00 , 'Coador', 6.90 , 'Mel', 10.00 , 'Café', 24.00)


for indice in range(0, len(produto_preço), 2):
    produto = produto_preço
    preço = produto_preço


print('--' * 30)
print('{:^60}'. format('TABELA DE PREÇOS:'))
print('--' * 30)


print(f'{produto[0]} {'--' * 10} {preço[1]}')
print(f'{produto[2]} {'--' * 10} {preço[3]}')
print(f'{produto[4]} {'--' * 10} {preço[5]}')
print(f'{produto[6]} {'--' * 10} {preço[7]}')
print(f'{produto[8]} {'--' * 10} {preço[9]}')




#Quarta tentativa:

produto_preço = ('Arroz', 23.00 , 'Feijão', 13.00 , 'Coador', 6.90 , 'Mel', 10.00 , 'Café', 24.00) 
for indice in range(0, len(produto_preço), 2): 
    produto = produto_preço[indice] 
    preço = produto_preço[indice + 1] 
    
print(produto) 
print(preço)




#Quinta tentativa:


produto_preço = ('Arroz', 23.00 , 'Feijão', 13.00 , 'Coador', 6.90 , 'Mel', 10.00 , 'Café', 24.00)


print('--' * 30)
print('{:^60}'. format('TABELA DE PREÇOS:'))
print('--' * 30)

for indice in range(0, len(produto_preço), 2):
    
    produto = produto_preço[indice]
    preço = produto_preço[indice + 1]
    print(f'{produto} {"--"*22:<40} R$ {preço:.2f}')

print('--' * 30)



#Como professor demonstrou:


listagem = ('Lápis', 1.75, 
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo ', 25,
            'Compasso', 9.99,
            'Mochila', 120.30,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)




