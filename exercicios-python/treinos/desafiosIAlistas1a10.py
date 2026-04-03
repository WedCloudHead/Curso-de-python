#EXERCÍCIO 1  [CORRIGIDO]

#Leia 8 números e:

#guarde em uma lista

#mostre:

#soma total

#média

#maior

#menor




somatotal = 0
maior = None
menor = None
lista = []


for numeros in range(8):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                lista.append(num)
                break
        except ValueError:
            print('Digite somente os valores sugeridos')

    
    somatotal += num

    if numeros == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

media = somatotal / 8        

print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')
print(f'A media dos numeros é {media:.2f}')
print(f'A soma dos numeros é {somatotal}')
print(f'Os numeros guardados dentro da lista são {lista}')







#EXERCÍCIO 2  [CORRIGIDO]

#Leia 10 números e mostre:

#quantos são pares

#quantos são ímpares

#lista apenas com os pares





total_pares = 0
total_impares = 0
pares = []


for _ in range(10):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                break
        except ValueError:
            print('Digite somente os valores sugeridos')

    if num % 2 == 0:
        total_pares += 1
        pares.append(num)
    else:
        total_impares  += 1


print(f'O total de números pares são: {total_pares}')
print(f'O total de números impares são: {total_impares}')
print(f'Apenas os números: {pares} são pares')
    






    #EXERCÍCIO 3 [CORRIGIDO]

    #Leia 7 números e:

    #mostre todos os números maiores que a média

    #mostre a quantidade deles




soma_numeros = 0
coleção = []
lista = []

for _ in range(7):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                coleção.append(num)
                break
        except ValueError:
            print('Digite somente os valores sugeridos')


    soma_numeros += num
    

#(Essa linha tambem pode ser uma condiçao, por exemplo: if len(coleção) > 0: )
media = soma_numeros / len(coleção)

for n in coleção:
    if n > media:
        lista.append(n)

quantidade = len(lista)


print(f'A quantidade de números acima da média são: {quantidade}')
print(f'Os numeros maiores que a média são: {lista}')
print(f'A média é: {media:.2f}')







#EXERCÍCIO 4 [CORRIGIDO]

#Leia 6 idades e:

#mostre a média

#quantas são maiores de 18

#qual a maior idade




soma_idade = 0
maior_idade = 0
lista = []


for c in range(6):
    while True:
        try:
            idade = int(input('Digite uma idade qualquer: '))
            if idade < 0:
                print('Digite apenas numeros positivos')
            else:
                lista.append(idade)
                break
        except ValueError:
            print('Digite somente os valores sugeridos')

    soma_idade += idade


    if c == 0:
        maior_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade

media = soma_idade / len(lista)

maior_18 = 0
for i in lista:
    if i > 18:
        maior_18 += 1


print(f'A media é {media:.2f}')
print(f'O total de pessoas com mais de 18 anos são: {maior_18}')
print(f'A maior idade é {maior_idade}')



#EXERCÍCIO 5 [CORRIGIDO]

#Leia 8 números e:

#crie duas listas:

#pares

#ímpares

#mostre ambas




pares = 0
impares = 0
lista = []


for numeros in range(8):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                lista.append(num)
                break
        except ValueError:
            print('Digite somente os valores sugeridos')


    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        


for p in lista:
    print()

for i in lista:
    print()

#IMCOMPLETO!!!


#CONCERTO: 10/10



list_pares = []
list_impares = []


for _ in range(8):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                break
        except ValueError:
            print('Digite somente os valores sugeridos')


    if num % 2 == 0:
        list_pares.append(num)
    else:
        list_impares.append(num)


print(f'A lista com pares possuem os números: {list_pares}')
print(f'A lista com impares possuem os números: {list_impares}')






#EXERCÍCIO 6 [CORRIGIDO]

#Leia 5 nomes e 5 notas:

#guarde nomes e notas

#mostre:

#nome do aluno com maior nota

#média da turma


maior_nota = 0
soma_valores = 0
nomes_maior_nota = []
lista = []

for contador in range(5):
    while True:
        try:
            nome = str(input('Digite um nome: ')).strip().capitalize()
            nota = float(input('Digite uma nota: '))
            if nota < 0 or nota > 10:
                print('Digite apenas valores de 0 a 10')
            else:
                break
        except ValueError:
            print('Digite os valores sugeridos')
        
    soma_valores += nota


    if contador == 0:
        maior_nota = nota
        nomes_maior_nota.append(nome)
    else:
        if nota > maior_nota:
            maior_nota = nota 
            nomes_maior_nota = [nome]
        else:    
            if nota == maior_nota:
                nomes_maior_nota.append(nome)


media = soma_valores / 5


print(f'Os aluno(s) com a mior nota: {nomes_maior_nota}')
print(f'A maior nota é: {maior_nota}')
print(f'A média das notas é {media:.2f}')




#EXERCÍCIO 7 (nível ↑) [CORRIGIDO]

#Leia 10 números:

#mostre quantos estão acima da média

#mostre o maior número acima da média


#Errado:

soma_numeros = 0
lista = []


for numeros in range(10):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                lista.append(num)
                break
        except ValueError:
            print('Digite somente os valores sugeridos')


    soma_numeros += num

media = soma_numeros / 10

maior_numero = 0
numeros_maior_que_media = 0
print(f'A media é {media:.2f}')
for numero in lista:
    if numero > media:
        numeros_maior_que_media +=1

    if numero > maior_numero:
        maior_numero = numero
        

print(f'Os numeros acima da media são: {numeros_maior_que_media}')
print(f'O maior numero da lista é {maior_numero}')


#Concerto:


soma_numeros = 0
lista = []
maior_numero = 0
numeros_maior_que_media = 0
lideres = []


for _ in range(10):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                lista.append(num)
                break
        except ValueError:
            print('Digite somente os valores sugeridos')


    soma_numeros += num

media = soma_numeros / len(lista)


print(f'A media é {media:.2f}')
for numero in lista:
    if numero > media:
        numeros_maior_que_media +=1
        if numero > maior_numero:
            maior_numero = numero
            lideres = [numero]
        elif numero == maior_numero:
            lideres.append(numero)
                        

        

print(f'Os numeros acima da media são: {numeros_maior_que_media}')
print(f'O maior numero da media é {maior_numero}')
print(f'Empate, se houver {lideres}')






#EXERCÍCIO 8 [CORRIGIDO]

#Leia 8 números:

#mostre a soma dos pares

#mostre a lista dos ímpares




#Incompleto:

soma_pares = 0
lista = []

for numeros in range(8):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros positivos')
            else:
                lista.append(num)
                break
        except ValueError:
            print('Digite os valores sugeridos')

    if num % 2 == 0:
        soma_pares += num

todos_impares = 0
for nu in lista:
    if nu % 2 == 1:
        todos_impares = nu

print(todos_impares)


#Refeito:



soma_pares = 0
lista_impares = []
lista_pares = []

for _ in range(8):
    while True:
        try:
            num = int(input('Digite um numero qualquer: '))
            break
        except ValueError:
            print('Digite apenas numeros')

    if num % 2 == 0:
        soma_pares += num
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f'O total de numeros pares na lista é {lista_pares}, e a soma dos numeros pares é {soma_pares}')
print(f'A lista com os numeros impares são {lista_impares}')









#EXERCÍCIO 9 (lógica forte) [CORRIGIDO]

#Leia 6 números:

#mostre:

#maior par

#menor ímpar

#(cuidado: pode não existir um dos dois)


#Errado:


maior_par = 0
menor_impar = 0
maior_num = 0
menor_num = 0
caixa = []

for cont in range(5):
    while True:
        try:
            num = int(input('Digite um numero inteiro qualquer: '))
            if num < 0:
                print('Digite apenas numeros acima de 0')
            else:
                caixa.append(num)
                break
        except ValueError:
            print('Digite os valores sugeridos')

    if cont == 0:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        if maior_num % 2 == 0:
            maior_par = maior_num
        else:
            if maior_num % 2 == 1:
                menor_impar = maior_num

    if num < menor_num:
        menor_num = num
    if menor_num % 2 == 1:
        menor_impar = menor_num
    else:
        if menor_num % 2 == 0:
            maior_par = menor_num


#Concerto:



maior_par = 0
menor_impar = 0
lista_pares = []
lista_impares = []

for contador in range(6):
    while True:
        try:
            num = int(input('Digite um número qualquer: '))
            break
        except ValueError:
            print('Digite apenas numeros')

    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
       
if lista_pares:
    maior_par = max(lista_pares)
    print(f'O maior par digitado foi: {maior_par}')
else:
    if not lista_pares: #Essa linha é redundante estou deixando pelo aprendizado, mas do else poderia partir direto pro print.
        print('A lista de pares está vazia!')
if lista_impares:
    menor_impar = min(lista_impares)
    print(f'O menor impar digitado foi {menor_impar}')
else:
    if not lista_impares: #Essa linha é redundante estou deixando pelo aprendizado, mas do else poderia partir direto pro print.
        print('A lista de impares está vazia!')
        
print('Fim do programa!!!')










#EXERCÍCIO 10 (desafio estilo prova 💥) [CORRIGIDO]

#Leia 10 números e mostre:

#média

#maior e menor

#quantos estão acima da média

#lista com os números acima da média

#lista com os números abaixo da média



#Incompleto: 



somanum = 0
maior_num = 0
menor_num = 0
guarda_num = []


for numeros in range(10):
    while True:
        try:
            num = int(input('Digite um número qualquer: '))
            if num < 0 or num > 10:
                print('Digite apenas numeros maiores que 0 e menores que 10')
            else:
                 guarda_num.append(num)
            break
        except ValueError:
            print('Digite os valores sugeridos')

    somanum += num

    if numeros == 0:
        maior_num = num
        menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        elif num < menor_num:
            menor_num = num
    
media = somanum / 10
maior_que_media = 0
menor_que_media = 0
for nu in guarda_num:
    if nu > media:
        maior_que_media += 1
    else:
        menor_que_media +=1



for maior_que_media in guarda_num:
    print(maior_que_media)


for menor_que_media in guarda_num:
    print(menor_que_media)


print(f'O maior numero é {maior_num}')
print(f'O menor numero é {menor_num}')
print(f'A media dos numeros é {media}')
print(f'O numeros maiores que a media são {maior_que_media}')
print(f'O numeros menores que a media são {menor_que_media}')




#Refeito:



soma_numeros = 0
maior = 0
menor = 0
lista = []

for contador in range(10):
    while True:
        try:
            num = int(input('Digite um número qualquer: '))
            lista.append(num)
            break
        except ValueError:
            print('Digite apenas numeros!')

    soma_numeros += num
    

    if contador == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        else:
            if num < menor:
                menor = num

media = soma_numeros / 10

num_menor_media = 0
num_maior_media = 0
lista_menor_media = []
lista_maior_media = []
for n1 in lista:
    if n1 > media:
        num_maior_media += 1
        lista_maior_media.append(n1)
    else:
        num_menor_media += 1
        lista_menor_media.append(n1)


print(f'A media é {media}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print(f'Os numeros acima da media são {num_maior_media}')
print(f'Os numeros abaixo da media são {num_menor_media}')
print(f'A lista com os numeros maiores que a média é {lista_maior_media}')
print(f'A lista com os numeros menores que a média é {lista_menor_media}')


#Perfeito!!! Matei a lista de 10 exercicios propostos pela IA.