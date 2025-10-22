#operadores aritmeticos:

#tipos de operadores em python:

n1 = 5 + 2   #operador de adição
n2 = 5 - 2   #operador de subtração
n3 = 5 * 2   #operador de multiplicação
n4 = 5 / 2   #operador de divisão
n5 = 5 % 2   #operador de resto da divisão
n6 = 5 // 2  #operador de divisão inteira
n7 = 5 ** 2  #operador de potenciaçao
print('os seguintes resultados de: ', (n1), (n2), (n3), (n4), (n5), (n6), (n7), ' respectivamente ')



#ordem de precedencia:

#1 ( )
#2 **
#3 * / // %
#4 + -

#sempre essa ordem a ser seguida nos problemas aritmeticos em python, lembrando que num possivel problema que apareça todos os operadores de uma so vez, basta seguir restritamente a ordem, primeiro resolve todos os parenteses, depois a potencia, depois mult, div, div int, div res, soma, sub


nu1 = int(input('any value: '))
nu2 = int(input('another value: '))
print('the results worth: {}'.format(nu1+nu2))


numb1 = int(input('any value: '))
numb2 = int(input('another value: '))
s = numb1 + numb2
m = numb1 * numb2
d = numb1 / numb2
di = numb1 // numb2
p = numb1 ** numb2
print('the sum is {} the multipication is {} the division is {} the rest of division is {} the exponentiation is {} '.format(s, m, d, di, p))



#extra:

#o terminal tem algumas funções de organização de print, algumas delas são: \n e end=' '

#\n se usa quando se quer qubrar uma linha por exemplo: print('the sum is {} \n the multipication is {} \n the division is {} \n the rest of division is {} \n the exponentiation is {} '
#essas linhas que tem o \n antes serao printadas uma em baixo da outra.

#end=' ' é justamente o contrario ao adicionar essa função no final de um comando print o proximo print automaticamente seguira na mesma linha onde terminou o ultimo print, essa função se usa assim:
#print('the sum is {} the multipication is {} the division is {} the rest of division is {} the exponentiation is {} '.format(s, m, d, di, p))end=' '
#o end=' ' ao final do print mostrara ao compilador que o proximo print pode começar na mesma linha