#Exercício 1 (contador simples)

#Faça um programa que leia 6 números inteiros.

#No final mostre:

#quantos números são pares

#quantos números são ímpares


#Resolução:



pares = 0
impares = 0
soma_pares = 0
for _ in range(6):
    while True:
        try:
            num = int(input('Digite um numero qualquer: '))
            break
        except ValueError:
            print('Digite apenas valores numéricos: ')


    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1

print(f'O total de números pares é {pares}')
print(f'O total de números impares é {impares}')
print(f'A soma de todos os numeros pares é {soma_pares}')




#Exercício 2 (contador + condição)

#Faça um programa que leia 5 idades.

#No final mostre:

#quantas pessoas são maiores de idade (18+)

#quantas são menores de idade


#Resolução:

maiores18 = 0
menores18 = 0

for _ in range(5):
    while True:
        try:
            usuario = int(input('Digite sua idade: '))
            if usuario < 0:
                print('Não pode ter números negativos')
            else:
                break
        except ValueError:
            print('Digite apenas valores numericos!')

    if  usuario >= 18:
        maiores18 += 1
    else:
        menores18 += 1

print(f'O total de idades acima de 18 é: {maiores18}')
print(f'O total de idade menores de 18 é: {menores18}')



#Exercício 3 (acumulador)

#Leia 5 números e mostre no final:

#a soma de todos os números

#a média dos números


soma_num = 0

for _ in range(5):
    while True:
        try:
            digite = int(input('Digite um número qualquer: '))
            break
        except ValueError:
            print('Digite apenas números!')

    soma_num += digite
media = soma_num / 5

print(f'A soma de todos os números é {soma_num}')
print(f'A média de todos os números é {media}')



#Exercício 4 (comparador)

#Leia o peso de 7 pessoas.

#No final mostre:

#o maior peso

#o menor peso

#(parecido com um que você já fez, mas com mais dados)




maior_peso = 0
menor_peso = 0

for contador in range(7):
    while True:
        try:
            pessoas = float(input('Digite seu peso: '))
            if pessoas < 0:
                print('Não pode adicionar pesos negativos!')
            else:
                break
        except ValueError:
            print('Digite de acordo com o que se pede!')

    if contador == 0:
        maior_peso = pessoas
        menor_peso = pessoas
    else:
        if pessoas > maior_peso:
            maior_peso = pessoas
        if pessoas < menor_peso:
            menor_peso = pessoas

print(f'O maior peso digitado é {maior_peso:.2f}')
print(f'O menor peso digitado é {menor_peso:.2f}')



#Exercício 5 (contador + filtro)

#Leia 10 números inteiros.

#No final mostre:

#quantos números são positivos

#quantos são negativos

#quantos são zero




numero_positivos = 0
numeros_negativos = 0
numeros_0 = 0

for _ in range(10):
    while True:
        try:
            digite = int(input('Digite um numero, pode ser negativo ou positivo: '))
            break
        except ValueError:
            print('Digite de acordo com o que se pede!')
        
    
    if digite == 0:
        numeros_0 += 1
    elif digite > 0:
        numero_positivos += 1
    else:
        numeros_negativos += 1

print(f'O total de numeros positivos são {numero_positivos}')

print(f'O total de numeros negativos são {numeros_negativos}')

print(f'O total de numeros 0 são {numeros_0}')




#Exercício 6 (comparador + nome)

#Leia os dados de 5 pessoas:

#nome

#idade

#Mostre no final:

#o nome da pessoa mais velha

#o nome da pessoa mais nova



nome_pessoa_velha = ''
idade_pessoa_velha = 0
nome_pessoa_nova = ''
idade_pessoa_nova = 0

for dados in range(5):
    while True:
        try:
            nomes = str(input('Digite seu nome: ')).strip().capitalize()
            idades = int(input('Digite sua idade: '))
            break
        except ValueError:
            print('Digite os valores sugeridos corretamente.')

    if dados == 0:
        idade_pessoa_velha = idades
        idade_pessoa_nova = idades
        nome_pessoa_velha = nomes
        nome_pessoa_nova = nomes
    else:
        if idades > idade_pessoa_velha:
            idade_pessoa_velha = idades
            nome_pessoa_velha = nomes
        elif idades < idade_pessoa_nova:
            idade_pessoa_nova = idades
            nome_pessoa_nova = nomes

print(f'A idade da pessoa mais velha é {idade_pessoa_velha} e seu nome é {nome_pessoa_velha}')
print(f'A idade da pessoa mais nova é {idade_pessoa_nova} e seu nome é {nome_pessoa_nova}')


        


#Exercício 7 (acumulador + condição)

#Leia 8 números.

#No final mostre:

#a soma apenas dos números pares
#o total de numeros pares


pares = 0
soma_pares = 0

for _ in range(4):
    while True:
        try:
            tecle = int(input('Digite um número inteiro qualquer: '))
            if tecle < 0:
                print('Digite apenas números inteiros')
            else:
                break
        except ValueError:
            print('Digite apenas o números sugeridos.')

    if tecle % 2 == 0:
        soma_pares += tecle
    if tecle % 2 == 0:
        pares += 1

    
print(f'Ao todo temos {pares} numeros pares e a soma de todos os numeros pares é {soma_pares}')

        




#Exercício 8 (contador + comparador)
 
#Leia os dados de 6 alunos:

#nome

#nota

#Mostre:

#a maior nota

#o nome do aluno com maior nota

#quantos alunos tiveram nota maior ou igual a 7


maior_nota = 0
nome_maior_nota = ''
tot_maior_igual = 0


for c in range(6):
    while True:
        try:
            nome = str(input('Digite seu nome:  ')).strip().capitalize()
            nota = float(input('Digite sua nota: '))
            if nota < 0 or nota > 10:
                print('Digite valores de 0 a 10.')
            else:
                break
        except ValueError:
            print('Digite os valores sugeridos.')

    if nota >= 7:
        tot_maior_igual += 1        

    if c == 0:
        maior_nota = nota
        nome_maior_nota = nome 
    else:
         if nota > maior_nota:
             maior_nota = nota
             nome_maior_nota = nome

print(f'A maior nota é {maior_nota} do(a) aluno(a) {nome_maior_nota}')
print(f'O total de {tot_maior_igual} alunos(a) tiraram 7 ou mais')




#Exercício 9 (combinação completa)

#Leia os dados de 5 pessoas:

#nome

#idade

#sexo

#Mostre no final:

#a média de idade do grupo

#o nome da mulher mais velha

#quantas pessoas têm mais de 30 anos



nome_mulher_velha = ''
pessoas_mais_30 = 0
soma_idade = 0
maior_idade = 0

for cont in range(5):
    while True:
        try:
            nome = str(input('Digite um nome: ')).strip().capitalize()
            idade = int(input('Digite uma idade: '))
            sexo = str(input('Digite o sexo [M/F]: ')).strip().lower()
            break
        except ValueError:
            print('Digite de acordo com as informções sugeridas.')

    soma_idade += idade 

    if idade > 30:
        pessoas_mais_30 += 1

    if sexo == 'f' and idade > maior_idade:
        nome_mulher_velha = nome 
        maior_idade = idade

print(f'A media de idade do grupo é de {soma_idade / 5:.0f} anos.')
print(f'O nome da mulher mais velha é {nome_mulher_velha} e ela tem {maior_idade} anos')
print(f'O total de {pessoas_mais_30} pessoas tem mais de 30 anos')







#Exercício 10 (desafio estilo prova)

#Leia 10 números inteiros.

#Mostre no final:

#o maior número

#o menor número

#a média dos números

#quantos números são maiores que a média


maior_numero = 0
menor_numero = 0
numeros_maior_media = 0
soma_tot_num = 0
numeros = []

for cont in range(10):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0 or num > 10:
                print('Digite valores de 0 a 10')
            else:
                numeros.append(num)
                break    
        except ValueError:
            print('Digite como é sugerido acima')

    soma_tot_num += num
    
    
    if cont == 0:
        maior_numero = num
        menor_numero = num
    else:
        if num > maior_numero:
            maior_numero = num

        if num < menor_numero:
            menor_numero = num
    
media = soma_tot_num / 10

for n in numeros:
    if n > media:
        numeros_maior_media += 1



print(f'O maior numero é {maior_numero}')
print(f'O menor numero é {menor_numero}')
print(f'A media dos numeros é {media}')
print(f'O total de {numeros_maior_media} numeros são maiores que a media')



#EXERCÍCIOS EXTRAS:


#Um exercício MUITO bom para o seu nível agora [corrigido]

#Esse aqui aparece muito em cursos de Python.

#Exercício

#Leia 10 números inteiros.

#Mostre:

#quantos números são pares

#quantos números são ímpares

#qual foi o maior número

#qual foi o menor número

#a média dos números



total_pares = 0
total_impares = 0
maior_num = 0
menor_num = 0
tot_num = 0

for cont in range(10):
    while True:
        try:
            numero = int(input('Digite um numero: '))
            if numero < 0:
                print('Digite somente numeros de 0 para cima')
            else:
                break
        except ValueError:
            print('Digite conforme sugerido')

    tot_num += numero
    
    if cont == 0:
        maior_num = numero
        menor_num = numero
    else:
        if numero > maior_num:
            maior_num = numero

        if numero < menor_num:
            menor_num = numero
    
    if numero % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
    
media = tot_num / 10
    
print(f'o total de numeros pares é {total_pares}')
print(f'O total de numeros impares é {total_impares}')
print(f'O maior numero é {maior_num}')
print(f'O menor numero é {menor_num}')
print(f'A media é {media}')



#Próximo exercício (um pouco mais interessante) [corrigido]

#Esse é muito comum em cursos.

#Exercício

#Leia 8 números inteiros.

#Mostre:

#quantos números são pares

#quantos números são ímpares

#a soma apenas dos números pares

#o maior número digitado

#Ou seja, você vai misturar:

#contador
#+
#acumulador
#+
#comparador




total_pares = 0
total_impares = 0
soma_pares = 0
maior_num = 0


for c in range(8):
    while True:
        try:
            numero = int(input('Digite um numero: '))
            if numero < 0:
                print('Digite somente numeros de 0 para cima')
            else:
                break
        except ValueError:
            print('Digite os valores sugeridos')

    if c == 0:
        maior_num = numero
    else:
        if numero > maior_num:
            maior_num = numero
        
    if numero % 2 == 0:
        total_pares += 1
        soma_pares += numero
    else:
        total_impares += 1


print(f'O total de numeros pares é {total_pares}')
print(f'O total de numeros impares é {total_impares}')
print(f'O maior numero digitado é {maior_num}')
print(f'A soma dos numeros pares é {soma_pares}')




#Próximo desafio (nível acima) [corrigido]

#Agora vou subir um pouco o nível — sem fugir do que você já sabe:

#Exercício novo

#Leia 6 números inteiros.

#No final, mostre:

#a soma de todos os números

#a média

#o maior número par

#o menor número ímpar

#Esse exercício vai te forçar a pensar:

#Você vai precisar combinar:

#filtro (par/ímpar)

#comparador condicionado


A_soma_tot = 0
maior_par = 0
maior_impar = 0

for contador in range(6):
    while True:
        try:
            tecle = int(input('Digite um numero: '))
            if tecle < 0:
                print('Digite apenas numeros positivos')
            else:
                break
        except ValueError:
            print('Digite os valores sugeridos')

    A_soma_tot += tecle

    if contador == 0 and tecle % 2 == 0:
        maior_par = tecle
    if contador == 0 and tecle % 2 == 1:
        maior_impar = tecle
    else:
        if tecle % 2 == 0 and tecle > maior_par:
            maior_par = tecle
        elif tecle % 2 == 1 and tecle > maior_impar:
            maior_impar = tecle

media = A_soma_tot / 6

print(f'O maior numero par é {maior_par}')
print(f'O maior numero impar é {maior_impar}')
print(f'A media entre todos os valores digitados é {media:.2f}')




#Como evoluir ainda mais (nível acima) 


#Leia 10 números inteiros.

#No final mostre:

#quantos números são positivos

#quantos são negativos

#quantos são zero


#Se quiser subir o nível desse exercício, dá pra transformar ele em:

#Versão avançada

#Além de contar, mostrar:

#soma dos positivos

#média dos negativos

#maior número digitado

#menor número digitado

#Isso mistura:

#contador + acumulador + comparador + filtro


#Próximo nível (desafio mais forte)

#Se quiser subir mais um nível, tenta isso:





soma_positivos = 0
media_negativos = 0
maior_numero = 0
menor_numero = 0
soma_negativos = 0

numero_positivos = 0
numeros_negativos = 0
numeros_0 = 0

for _ in range(10):
    while True:
        try:
            digite = int(input('Digite um numero, pode ser negativo ou positivo: '))
            break
        except ValueError:
            print('Digite de acordo com o que se pede!')
        

    if digite < 0:
        soma_negativos += digite
    if digite == 0:
        maior_numero = digite
        menor_numero = digite
        numeros_0 += 1
    else:
        if digite > maior_numero:
            maior_numero = digite
        elif digite < menor_numero:
            menor_numero = digite
        if digite > 0:
            numero_positivos += 1
            soma_positivos += digite
        else:
            numeros_negativos += 1

media = soma_negativos / 10

print(f'O total de numeros positivos são {numero_positivos}')
print(f'O total de numeros negativos são {numeros_negativos}')
print(f'O total de numeros 0 são {numeros_0}')


print(f'A soma dos numeros positivos é {soma_positivos}')
print(f'A soma dos numeros negativos é {soma_negativos}')
print(f'O maior numero digitado é {maior_numero}')
print(f'O menor numero digirado é {menor_numero}')
print(f'A media dos numeros negativos é {media:.2f}')




#Novo desafio [INACABADO IGUAL OBRA DA PREFEITURA]

#Leia 7 números.

#Mostre:

#maior número

#menor número

#média

#quantos são pares

#quantos são ímpares

#maior número par

#menor número ímpar

#Esse exercício junta TUDO que você aprendeu até agora.




maior_num = 0
menor_num = 0
total_pares = 0 
total_impares = 0
maior_par = 0
maior_impar = 0
soma_numeros = 0
lista = []

for numeros in range(7):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite somente numeros positivos')
            else:
                lista.append(num)
                break
        except ValueError:
            print('Digite os valores sugeridos')

    soma_numeros += num

    if numeros == 0:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        elif num < menor_num:
            menor_num = num

    if num % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1



media = soma_numeros / 7


#Está faltando o maior numero par e o maior numero impar.

print(f'O maior numero digitado é {maior_num}')
print(f'O menor numero digitado é {menor_num} ')
print(f'O maior numero par digitado é {maior_par} e possuem ao todo {total_pares} numeros pares digitados')
print(f'O maior numero impar digitado é {maior_impar} e possuem ao todo {total_impares} numeros impares digitados')
print(f'A media dos numeros é {media:.2f}')



