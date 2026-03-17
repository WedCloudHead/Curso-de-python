#02)

n = int(input('Digite um número: '))
for w in range(0, n):
    print(w)
print('Fim')

#Nesse exemplo temos que na linha 4 for w in range(0, n): sendo n o input
#acima significa que o contador vai contar de 0 ate um numero antes do valor
#dado no imput, isso é muito útil para resolver problemas específicos

n = int(input('Digite um número: '))
for w in range(0, n+1):
    print(w)
print('Fim')

#Nesse exemplo temos que na linha 4 for w in range(0, n+1): sendo n o input
#acima significa que o contador vai contar de 0 ate o numero exato do valor
#dado no imput, pois esse +1 ao final significa que ele tem que considerar
#um algarismo a mais 
#isso é muito útil para resolver problemas específicos.

n = int(input('Digite um número: '))
for w in range(10, n+1, 2):
    print(w)
print('Fim')

#Nesse exemplo assim como no aula013.py serve o mesmo proposito, ele ira
#contar de 10 até o numero escolhido pelo input n, somando mais um algarismo 
#ao final se possivel, e pulando de 2 em 2 ate o fim.


n = int(input('Digite um número: '))
for w in range(10, n-1, -1):
    print(w)
print('Fim')

#Aqui é exatamente como anterior só que em vez dele executar em ordem
#crescente, será em ordem decrescente, então se for adicionado no input
#um numero maior que 10 ele nem conta, ja vai direto pro print fim.

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('Fim')