#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. 



#Primeira tentativa:  

numero = 0
primeiro_termo = None
razao = None

while primeiro_termo:
    try:
        primeiro_termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razão da PA: '))
        if primeiro_termo < 0:
            print('Digite somente valores acima de 0')
        if razao < 0:
            print('Digite somente valores acima de 0')
    except ValueError:
        print('Digite somente os valores sugeridos')

resultado = primeiro_termo * razao
print(resultado)

while resultado < 11:
    print(resultado)



#Segunda tentativa:

usuario = int(input('Digite o primeiro termo da PA: '))
usuario2 = int(input('DIgite a razão da PA: '))
for contador in range(0, usuario, usuario2):
    print(contador)
while contador < 11:
    print(contador)

print('Fim do programa!')



#Terceira resolução:


while True:
    try:
        termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razão da PA: '))
        break
    except ValueError:
        print('Digite apenas valores numericos!')


contador = 0      
print('Os 10 primeiros termos da PA: ')
while contador < 10:
    print(termo, end=', ')
    termo += razao
    contador += 1

print('Fim do programa!')
    
 


#Resolução do professor: 

print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' -> ')
    termo += razão
    cont += 1
print('FIM')



#Info extra: 
#A lógica da PA é: an = a1 + (n − 1)r


#Resolução das aulas:
