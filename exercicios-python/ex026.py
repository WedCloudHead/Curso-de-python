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


#treinando mais um pouco:

#caça palavras, quantas vezes aparece a letra "a/A", "d/D", "t/T" no texto, identifique a autora do texto, qual a ultima palavra do texto e tambem entregue um resulltado final separando todas as palavras por grupos e mostre quantos grupos de palavras tem ao todo:

texto = str('Hino à vida -por Lou Salomé: Tão certo quanto o amigo ama o amigo, Também te amo, vida-enigma Mesmo que em ti tenha exultado ou chorado, mesmo que me tenhas dado prazer ou dor. Eu te amo junto com teus pesares, E mesmo que me devas destruir, Desprender-me-ei de teus braços Como o amigo se desprende do peito amigo. Com toda força te abraço! Deixa tuas chamas me inflamarem, Deixa-me ainda no ardor da luta Sondar mais fundo teu enigma. Ser! Pensar milênios! Fecha-me em teus braços: Se já não tens felicidade a me dar Muito bem: dai-me teu tormento').strip().upper()

print(' As letras a/A aparecem {} vezes no texto\n as letras d/D aparecem {} vezes no texto\n as letras t/T aparecem {} vezes no texto '.format(texto.count('A'), texto.count('D'), texto.count('T')))

print('A autora do texto é: {} '.format(texto[17:27]))

separa = texto.split()

print('A ultima palavra do texto é: {} '.format(separa[len(separa)-1]))

print('ao todo esse texto tem:', len(separa), 'caracteres')




#extra:
#nas linhas: 35/37/39 ao final do codigo tem esse +1 que simplismente significa que quando o metodo encontrar o caracter que voce pediu, ele vai adicionar + 1 isso se usa pq na programação começa a se contar pelo 0 e não pelo 1 entao a caracter que esteja na posição 5 por exemplo seria mostrado no programa como posição 4, esse +1 simplismente ajusta somando + 1 caracter no final. 
#(tambem pode por +2, +12 ou -1, -33; qualquer numero, somando ou subtraindo, o resultado vai ser a mesma logica, ele ira somar ou subtrair a quantidade de caracter no final)
