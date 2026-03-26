#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, 
#desconsiderando os espaços.

#Ex: apos a sopa (sem espaços de tras pra frente)


#Como eu fiz:

digite = str(input('Digite a frase para saber se é um palíndromo: ')).lower().strip()
espaço = digite.replace(" ", "")
detras = espaço[::-1]

if espaço == detras:
   print('É um palindromo')
else:
    print('Não é um palindromo')
print('Fim do programa!')



#Segunda resolução:

digite = str(input('Digite uma frase para saber se é um palíndromo: ')).lower().strip()

frase = digite.replace(" ", "")

invertida = ""

for i in range(len(frase) - 1, -1, -1):
    invertida += frase[i]

if frase == invertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

print('Fim do programa!')



#Ao fim da resolução do professor virar a explicação desse meu novo método que usei para refazer o exercicio.



#Como o professor demonstrou:

frase = str(input('Digite uma frase: ')).strip().upper() 
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndrimo!')
else:
    print('A frase digitada não é um palindromo!')
     




#1) Primeira resolução: 
#É uma forma simplificada de resolver o problema, inclusive é mais usada por programadores mais
#experientes, resolve o problema dos palíndromos porém, não é o que o professor pediu que foi
#resolver esse problema utilizando o laço for.
#Basicamente na (linha 10) a variavel espaço recebe digite.replace(" ", "") essa linha serve
#para retirar os espaços de dentro da string, ou seja, o que antes era wed da silva torres, 
#agora fica weddasilvatorres e essa é a primeira chave para resolver um palíndromo.
#Na (linha 11) a variavel detras = espaço[::-1] serve para inverter a ordem da string e ler ela
#de tras para frente. Chamado de slicing reverso, basicamente python vira nohtyp por exemplo.
#O restante é apenas condição padrão, se espaço == detras ou seja, se de tras para frente for 
#identico ao de frente para tras sem espaços, é um palíndromo, caso contrário, não.


#2) Segunda resolução:
#Infeslimente eu tive apoio da IA para resolver o problema nessa segunda resolução, o que me 
#resta agora é no mínimo aprender com ela;
#(linha 23) Ler e padronizar a frase; input, .lower() e .strip()
#(linha 25) Remover os espaços da frase; frase = digite.replace(" ", "")
#(linha 27) Criar uma variável vazia; invertida = "" e aqui está o pulo do gato também.
#(linha 29) O for que percorre a palavra o contrário; for i in range(len(frase) - 1, -1, -1):
#E aqui nessa linha onde tem algo que foi novidade pra mim esse "len" dentro do for que já pega
#o tamanho total da string contada e automaticamente sem espaços graças a linha 25.
#E o range (linha 29) que tem em seus parenteses -1, -1, -1) funciona assim:
# inicio = ultima posição, fim = -1 e passo = -1 ou seja 5,4,3,2,1,0, ele anda para trás.
#(linha 30) dentro do for; invertida += frase[i] vamos entender isso:
#Se frase = "python" primeira volta: i = 5 frase[5] = n (n do fim da palavra python)
#Então: invertida = "" + "n" vira: invertida = "n"
#Segunda volta: i = 4 frase[4] = o (o da penultima letra da palavra python)
#Agora: invertida = "no" e assim por diante ate formar: "nohtyp"
#(linha 32) comparando as duas frases; if frase == invertida:
#Se frase = radar, invertida = radar então é palindromo mas se frase = python e invertida = 
#nohtyp então não é palindromo.



# Sobre a resolução do professor:
#Segue um raciocinio muito parecido com a segunda resolução a diferença está principalmente 
#nas (linhas 48) palavras = frase.split() e (linha 49) junto = ''.join(palavras)
#que servem quase que igualmente as linhas 25 e 27 da segunda resolução.
#A diferença é que a linha 48 pega a string e separa todas letras numa especie de lista
#enquanto a linha 49 junta todas essas letras numa so frase.
#Dai todo seguimento a seguir é identico a segunda resolução.









