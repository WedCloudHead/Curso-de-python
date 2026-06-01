
#variável simples:
lanche = ('hambúrguer')
print(lanche)


#Tupla:
lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche)


#Acessando índices dentro das tuplas:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim') #(UM PARENTESES PARA ESSE FORMATO QUE LÊ O ÍNDICE DE ACORDO COM INPUT DADO)
opção = int(input())
print(lanche[opção])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[1])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[3])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[-2])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[-1])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[1:])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[:3])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[1:3])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[-2:])

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
print(lanche[-3:])


#Provando a imutabilidade das tuplas:
#(esta entre parenteses para não quebrar todo os programas)
'''

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
lanche[1] = 'Refrigerante'
print(lanche[1])  

'''
#Ao tentar executar esse código de cima o python retornara erro, dizendo que o item sugerido não pode ser assimilado.



#Mostrando o uso da tupla no for:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muito!')


    

#Mostrando uso do len em tuplas:


lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim' , 'batata frita')

#Por ter um alimento a mais ele mostrara o valor 5
print(len(lanche))


lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

print(f'Ao todo eu comi e bebi {len(lanche)} alimentos')



#Junção do len + for:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche}')
print('Comi muito!')
    

#Esse segundo exemplo se assemelha muito ao uso do for normal:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi muito!')
    


#Mostrando que o uso do len é muito util para pegar a posição de cada elemento:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

for cont in range(0, len(lanche)):
    print(f'O grupo de alimentos: {lanche} na posição {cont}')
print('Fim!')
    

#Trabalhando com 2 tuplas:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

#Aqui é possível ver o exemplo de atribuição de tuplas e o que acontece aqui quando se soma 
#a + b é que se cria uma nova tupla c que mostra a junção de ambas a + b e não soma elas.


#Também é possível ordenar as tuplas com sorted:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(c))



#Len de soma de tuplas:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))



#Quantas vezes aparece um elemento em especifico dentro de uma tupla:


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))

#O que o count faz é mostrar quantas vezes o número 5 aparece dentro de c.



#Posição com propriedade de cada elemento:


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(8)) #(poderia ser qualquer valor dentro da tupla)

#O que o index faz nesse exemplo é mostrar em qual posição da tupla está o elemento 8
 
#Como achar o item com propriedade repetida ficaria muito grande pra explicar, basta 
#acessar esse link: https://youtu.be/0LB3FSfjvao?si=PWd2wekk9SxWzDz2&t=2332  onde da pra ver detalhadamente.




#É possível conjulgar valores númericos e valores str em tuplas:

pessoa = ('Pedro', 39, 'Masculino', 55.60)

print(pessoa)

#Esse trecho mostra que python não faz restrição na hora da leitura, porém é importante lembrar que nesse formato
#python está tratando tudo como str números e letras.






#EXTRA:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

for pos, comida in enumerate(lanche):
    print(f'O lanche {comida} está na posição: {pos}')
print('Fim!')
    

#Nesse extra é possível ver que da pra adicionar mais de uma variável em for como vista
#esse for possue as variáveis pos e comida e a função enumerate que enumera os itens muito parecido com len
#Então a primeira variável sempre vai pegar o elemento e a segunda a posição.



#Método sorted:

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')

print(sorted(lanche)) #Esse print ajusta os elementos dentro da lista em ordem.

#Porem como dito antes, tuplas são imutaveis, então o que sorted faz é ordenar apenas para aquele
#print em especifico se verificar nesse novo print, a tupla original se mantém:

print(lanche)



#Como apagar informações de uma tupla:

exemplo = (1, 2, 3, 4)

del(exemplo)
print(exemplo)


#Porém não é possível apagar somente 1 elemento dentro da tupla:
#Está entre aspas para não dar erro no código

'''

exemplo = (1, 2, 3, 4)

del(exemplo[2])
print(exemplo)

'''