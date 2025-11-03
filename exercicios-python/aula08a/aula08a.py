#import de modulos na pratica:
#01) import generalizado/comum:

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {} '.format(num, math.ceil(raiz))) #lembrando que caso queira mostrar outras funcionalidades, basta mudar ceil por floor, factorial, etc, caso queira considerar somente os dois numeros apos o ponto basta apagar math. e colocar dentro de {} o comando {:.2f} como ja foi aprendido 


#2) import especifico:

from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {:.2f} '.format(num, raiz))
#aqui vemos na pratica a diferença entre o import generalizado e o especifico, nesse segundo exemplo vemos que o compilador python ira trazer da sua biblioteca math somente o modulo sqrt assim trabalhando diretamente com o que o programador quer e reduzindo o tamanho do arquivo que é importado para memoria do pc.


#3) import especifico:

from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {:.2f} '.format(num, floor(raiz)))
#bem parecido com import anterior, nessa declaração esta sendo usado os modulos especificos: sqrt e floor






#Importante:

#1)
#na linha 1 é possivel ver a importação math da biblioteca: import math
#é importante entender que na linha 3 ao utilizar o modulo: math.sqrt so é possivel graças a esse import feito na linha 1 pois sem ele o python não conseque carregar da sua biblioteca essa funcionalidade.

#na linha 4 em format(num, math.ceil(raiz))
#a adição do modulo math.ceil(raiz) so possivel graças ao import math tambem, nota-se que ao usar esse modulo o compilador python ira automaticamente/matematicamente arrendondar (para cima) todos os resultados de raizes quadradas.


#2)
#na linha 14 é importante notar que a forma de declarar mudou de um import para o outro, no import simples usou:
#aiz = math.sqrt(num)
#enquanto no import especifico usou:
#raiz = sqrt(num)
#pois no segundo import não precisava especificar sqrt pois na linha 12 ja esta especificado.


#3)
#na linha 22 é adicionado o modulo floor que especifica ainda mais o import de math e tras da biblioteca somente esses dois modulos

#é tambem da pra ver a diferença de declaração nas linhas 25, 15 e 7 onde na 25 não se usa math.floor(raiz) e sim somente floor(raiz) pois o math. so é preciso quando não se especifica no import inicial como é a diferença entre as linhas 4 e 22.


#extra:

#para saber quais importações por padrao ha nas bibliotecas python basta dar uma analizada nesse trecho:
# https://youtu.be/oOUyhGNib2Q?si=bkql-yvF4_Mrl9pf&t=1091
#porem resumidamente basta acessar pyhton.org site original python, ir em docs ou documentação e procurar de acordo com a versão atual do seu python quais as bibliotecas disponiveis no momento para importação.