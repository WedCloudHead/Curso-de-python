#escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# -1 para binário
# -2 para octal
# -3 para hexadecimal


#como eu fiz:

#Não soube fazer :(

#como professor demonstrou:

numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] coverter para bínario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{numero} convertido para bínario é igual a:', bin(numero)[2:])
elif opção == 2:
    print(f'{numero} convertido para octal é igual a:', oct(numero)[2:])
elif opção == 3:
    print(f'{numero} convertido para hexadecimal é igual a:', hex(numero)[2:])
else:
    print('Essa opção é inválida, tente novamente!')


#Anotação sobre a aula:

#Sobre a linha 15 a 18, é usado um novo metodo no print na linha 15, um print com ''' ''' três aspas simples de cada lado, isso nada mais é que uma forma mais livre de você escrever seu print no terminal, ou seja, se estiver escrevendo algo em uma linha e pular pra linha de baixo, quando for printado no terminal também estara na linha de baixo.

#Para a explicação sobre as linhas 21, 23 e 25 foi adicionado ao fim dos prints os parametros bin(numero), oct(numero) e hex(numero) nada mais são que o proprio python convertendo o numero do input dado em bínario, octal e hexadecimal, pois a biblioteca python ja tem em seu acervo essas conversões prontas.

#Sobre os números [2:] ao final dos prints das linhas 21, 23 e 25, nada mais são que o método de fatiamento de strings, onde 2 significa em que posição você quer que o python comece a considerar as strings e : vaizio na frente significa que ele não tem um número limite para parar, ele pode ir considerando todas as letras até o final.


#Sobre esse problema eu não sabia sobre a função do python de conversão integrada que ele possui que são: bin(bínario), oct(octal) e hex(hexadecimal)
#porém de qualquer forma isso não é desculpa pois eu poderia ter ido atrás de respostas, ido procurar na biblioteca python, na internet, foruns, para saber mais sobre essas funções.
#mas de toda forma, cada desafio é um aprendizado, ainda não sei as duas bases númericas octal e hexadecimal mas pelo menos agora eu ja sei bínario, graças a esse exercício.



