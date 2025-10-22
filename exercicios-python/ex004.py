#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('tap something: ')
print('the primitive type of this value is ', type(a))
#o type type(a) faz o compilador analizar se é uma string essa declaração mesmo sabendo que qualquer declaração que comece sem nenhum tipo primitivo o compilador ira apontar que é uma string 
print('is it only spaces?', a.isspace())
#o type a.isspace() é usado para que o compilador analise se na declaração tem realmente letras, numeros ou somente espaços
print('is it a number?', a.isnumeric())
#o type a.isnumeric() serve para o compilador analisar se nessa declaração a numeros tambem
print('is it alphabetic', a.isalpha())
#o type a.isalpha() faz o compilador analizar se essa declaração é alfabetico 
print('is it alphanum', a.isalnum())
#o type a.isalnum() faz o compilador analizar se na declaração a letras e numeros juntos 
print('is it lower case? ', a.islower())
print('is it upper case? ', a.isupper())
# o type a.islower() e a.isupper() faz o compilador analizar se na declaração tem letras maiusculas e minusculas
print('is it captalized? ', a.istitle())
#o type a.istitle() faz o compilador analizar se na declaração existem palavras capitalizadas





#extra:
#importante ressaltar que todo a antes do ponto como a.isnumeric, a.isspace, a.salpha, etc.. tem relação direta com o que foi declarado no inicio que foi a = input('...') se fosse b = input ou dorflex = input, o parametro deixaria de ser a e passaria a ser o que foi escrito na delcaração

#lembrando que idependente do que é escrito no input o compilador ira devolver uma resposta que esse tipo primitivo é uma string(str) pois na declaração a = input eu não especifiquei que tipo primitivo eu estou declarando se eu quisesse declarar um tipo numero por exemplo eu teria que declarar algo como a = int(input('qualquer coisa')) ou a = float(input('qualquer coisa'))

#é importante notar que se tiver uma declaração com espaço e uma palavra ou numero juntos o compilador vai alegar false para number e para space por exemplo:
#digite o valor:45 (sem espaço) 
#number: true space: false
#digite o valor: 45 (com espaço)
#number: false space: false 

#na analise a.isalpha() que faz o compilador analizar se algo é alfabetico é importante notar que ele pode retornar false se tiver numero juntos por exemplo: gustavo é alfabetico mas gustavo13 nao é alfabetico é alfanumerico.
#lembrando tambem que apenas letras tambem é alfanumerico mas nao é alfabetico