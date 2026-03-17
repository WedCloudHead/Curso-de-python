#01)

#Exemplo 01:

for oi in range(1, 6):
    print('Hello friend')
print('FIM')


#Lembrando que "oi" na declaração é opcional
#Importante notar que em python ele não irá considerar o ultimo comando 
#dentro dos ( ) ou seja, ele não criara uma repetição de 'hello friend' de 1 
#ao 6 pois ele nunca considera o último número, caso eu queira que ele repita
#6 vezes eu tenho que colocar range(0, 6) dessa forma terão 6 repetições.

for oi in range(0, 6):
    print('Hello friend')
    print('FIM')

#Ainda dentro do exemplo 01 aqui pode se notar que o último print não está 
#indentado como no exemplo acima, dessa forma o python entende que o print
#(FIM) também deve ser repetido 6 vezes, enquantp np exemplo acima com a 
#indentação ele não estara sujeito a estrutura de repetição.



#Exemplo 02:

for oi in range(0, 6):
    print(oi)
print('FIM')

#Nesse exemplo 02 é possivel notar que em vez de ('Hello friend') dentro do
#parenteses existe ('oi') ou seja, o que foi declarado a cima, em vez do 
#python escrever hello friend 6 vezes ele escrevera 0 a 6.



#Exemplo 03:

for oi in range(6, 0):
    print(oi)
print('FIM')

#Nesse exemplo 03 é dado o comando (6, 0) e o python só responde com o print
#abaixo de ('FIM') pois ele não entende dessa forma que você quer uma
#contagem de 6 ao 0.


for oi in range(6, 0, -1):
    print(oi)
print('FIM')

#Ainda no exemplo 03 agora sim é demonstrado a forma correta de fazer com que
#ele conte de forma decrescente, esse '-1' adicionado no final é chamado de 
#iteração, é como se fosse um sinal para o python pra ele saber que você quer
#ir tirando de -1 em -1 do 6 até 0.

for oi in range(0, 7, 2):
    print(oi)
print('FIM')

#Ainda sobre o iteração nesse exemplo o que o python vai fazer é contar de 
#0 a 6 pulando de 2 em 2 pois foi adicionado esse 2 ao final como iteração.
#É importante entender cada comportamento das iterações e das repetições para
#que possam ser usadas como ferramentas e não algo que atrapalhe o programa.


#Extra:
#essa estrutura mais simples tem como foco a estrutura chamada variável de 
#controle que é representada especificamente por aquela declaração "oi" que 
#usei, essa declaração pode ser qualquer coisa, porém é chamada de variável
#de controle    