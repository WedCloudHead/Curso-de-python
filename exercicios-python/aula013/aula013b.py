#03)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('Fim')

#Nesse exemplo fica mais claro sobre como funciona o inicio, fim e a iteração
#dentro de um laço de repetição, com cada qual cumprindo especificamente seus
#deveres.


for c in range(0, 3):
    n = int(input('Digite um valor: '))
    print('FIm')

#Nesse exemplo fica claro que a indentação é muito 
#importante na execução do laço de repetição, pois
#a declaração n = input esta dentro de for c in
#range que é o laço de repetição, então
#automaticamente o n = input cai em repetição.



s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n  #(s += n)
print(f'O somatório de todos os valores foi de {s}')

#Esse exemplo é bom para demonstrar que uma variável
#mesmo que declarada a princípio fora do laço de 
#repetição pode ser adicionada nele, a variável s
#foi criada antes de tudo com s = 0 e na linha 30
#ele é adicionado ao laço de repetição com s = s + n
#ou seja o laço fará com que s receba s + n quantas
#vezes estiver estipulado dentro da repetição na
#linha 28, nesse caso 4.
#isso fara com que s some com mais n várias vezes
#até completar as 4x.
    
