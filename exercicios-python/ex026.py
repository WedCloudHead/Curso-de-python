#faça um programa que leia uma frase pelo teclado e mostre:

#quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez


# como eu fiz: 

frase = input('Digite uma frase: ')

print(frase.count('a'))

print(frase.find('a'))

print(len(frase))

 #dessa forma que eu fiz é possivel notar que o programa não atende 66,12% do problema pois so a linha 12 consegue resolver 1/3 do problema

 #tentando concertar:

frase = str(input('Digite uma frase: '))

print('nessa frase tem', frase.count('A'), 'letras "A" maiusculas e', frase.count('a'), 'letras "a" minusculas') 


print('a primeira letra "a" aparece na posição: {}, e a primeira letra "A" aparece na posição: {} '.format(frase.find('a'), frase.find('A')))

#Nao consegui resolver a ultima questao mas pelo menos agora ja foram 2/3 de acertos.

#como professor demonstrou:

frase = str(input('digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase. '.format(frase.count('A')+1))

print('A primeira letra A aparece na posição {} '.format(frase.find('A')+1))

print('A ultima letra A aparece na posição {} '.format(frase.rfind('A')+1))


#extra:
#nas linhas: 35/37/39 ao final do codigo tem esse +1 que simplismente significa que quando o metodo encontrar o caracter que voce pediu, ele vai adicionar + 1 isso se usa pq na programação começa a se contar pelo 0 e não pelo 1 entao a caracter que esteja na posição 5 por exemplo seria mostrado no programa como posição 4, esse +1 simplismente ajusta somando + 1 caracter no final. 
#(tambem pode por +2, +12 ou -1, -33; qualquer numero, somando ou subtraindo, o resultado vai ser a mesma logica, ele ira somar ou subtrair a quantidade de caracter no final)
