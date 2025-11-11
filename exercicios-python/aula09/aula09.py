#fatiamento:

frase = 'Curso em Video Python'
print(frase)   

frase = 'Curso em Video Python'
print(frase[3])

frase = 'Curso em Video Python'
print(frase[:13])

frase = 'Curso em Video Python'
print(frase[13:])

frase = 'Curso em Video Python'
print(frase[1:15:21])

frase = 'Curso em Video Python'
print(frase[3::2])

frase = 'Curso em Video Python'
print(frase[::4])

#analise:

frase = 'Curso em Video Python'
print(frase.count('o'))

frase = 'Curso em Video Python'
print(frase.count('O'))

frase = 'Curso em Video Python'
print(frase.upper().count('O'))
#nesse exemplo esta sendo atribuido um método de análise 
#com outro ou seja, fazendo todas as letras o se tornarem maiusculas com upper e fazendo a contagem delas com count

frase = 'Curso em Video Python'
print(len(frase))

frase = 'Curso em Video Python'
print(frase.find('urso'))

frase = 'Curso em Video Python'
print(frase.find('Android'))

frase = 'Curso em Video Python'
print('Curso' in frase)

frase = 'Curso em Video Python'
print('video' in frase)

frase = 'Curso em Video Python'
print(frase.lower().find('video'))

#transformação:

frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android'))
# vs
print(frase)
#acima vemos na pratica o que foi dito nas anotações de teoria em que na linha 49 mesmo dando o comando para que altere as palavras Python para Android, ele so mudara naquela instancia, a frase original segue imutavel


frase = 'Curso em Video Python'
print(frase.lower())

frase = 'Curso em Video Python'
print(frase.upper())

#divisão:

frase = 'Curso em Video Python'
print(frase.split())

frase = 'Curso em Video Python'
print('-'.join(frase))










#extra:
#caso seja preciso printar um trecho muito grande de algo

#print("""nesse exemplo você esta perguntando se existe a palavra Curso dentro da string mas diferente de mostrar o numero onde começa essa frase ele apenas retornara (true) que quer dizer que sim, existe essa palavra dentro da string, essa é função do operador in em python, responder se o que você esta procurando é true ou false, verdadeiro ou falso.""")

#basta adicionar 3 aspas duplas no inicio e fim do print