#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

#eu fiz assim:

n1 = int(input('any number: '))
n2 = int(n1 * 2) 
n3 = int(n1 * 3) #se quisesse a terça parte: n3 / 3
n4 = int(n1 ** 2)
res = (n2, n3)
print('o dobro de {} é: {} '.format(n1, n2))
print('o triplo de {} é: {} '.format(n1, n3))
print('a raiz quadrada de {} é: {} '.format(n1, n4))


#como o professor demonstrou na correção:

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2) # A utilização do parenteses é usada para forçar a execussao dessa conta primeiramente, pois o compilador python por padrão resolve exponenciaçao primeiro  
print('o dobro de {} vale {}. '.format(n, d))
print('o triplo de {} vale {}. \nA raiz quadradada de {} é igual a {:.2f}. '.format(n, t, n, r))


#forma compacta de se fazer tambem:

n = int(input('Digite um numero: '))
print('o dobro de {} vale {}. '.format(n, (n*2)))
print('o triplo de {} vale {}. \nA raiz quadradada de {} é igual a {:.2f}. '.format(n, (n*3), n, (n**(1/2))))

#sendo a diferença entre eles é que o calculo (linha 18, 19) d = n *2, t = n * 3; foram substituidos pelos calculos dentro do proprio print (linha 29).

#extra:
#importante lembrar que na linha 29 onde esta escrito \nA raiz quadrada... esse \n significa que a partir da letra A a frase começara na linha de baixo, esse \n nada mais é que uma quebra de linha no terminal.

#importante lembrar que na linha 29 onde esta escrito é igual a {:.2f} significa que o terminal levara em cinsideração apenas 2 casas decimais apos o ponto flutuante ou seja, o resultado da potencia que antes dava 5.744562646... agora dara 5.74

#importante lembrar que no lugar de n ** (1/2) que é a formula para descobrir a raiz quadrada de n, tambem da pra fazer assim pow(n, (1/2)) sendo que pow significa potencia e n, (1/2) a formula comum como efetuada normalmente.