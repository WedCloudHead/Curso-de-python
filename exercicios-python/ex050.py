#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
#daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

#Como eu fiz:



s = 0
for c in range(1, 7):
    numero = int(input('Digite um  numero:'))
    s = s + numero
if s % 2 == 1:
    print(s)
    print('O programa só entrega o resultado da soma se a soma resultar em par!')
else:
    print(f'A soma entre os numeros digitados é: {s}')
print('Fim do programa!')


#Após voltar treinando e praticando esse foi meu segundo modo de refazer o desafio (03/03/2026):


for c in range(1, 7, 1):
    usuario0 = int(input('Digite um numero par qualquer: '))
    impar = int(1)
    if usuario0 % 2 == impar:
        print('Esse numero é impar!')
    else:
        print(f'A soma entre {usuario0} + {usuario0} é igual a:', usuario0 + usuario0)
print('Fim da contagem!')


#Ao fim da resolução do professor virar a explicação desse meu novo método que usei para refazer o exercicio.



#Como o professor demonstrou:

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} numeros pares e a soma foi {soma}')



# Sobre a linha 8 a primeira tentativa minha foi meio que uma junção de lógica com alguns buracos e um pouco de um mal direcionamento conclusivo. 
# Eu até segui uma ordem okay, porém me embolei ao dar os comandos corretos!

# Sobre 23 em diante, ao refazer o exercicio após quase 2 meses parado ainda sim eu tive um ganho de pensamento lógico sobre o problema e os buracos essenciais foram praticamente batidos, o problema do meu programa está mais para um erro de contexto do que de fato de solução.
# Acontece que meu programa cobre o pedido que é excluir os numeros impares dos resultados do input e somar os pares, isso meu programa entrega brilhantemente, o problema é que ele não entrega a soma total de todos os pares no final e somente as somas individuais.


# Sobre a resolução do professor: 
# É explicdo de maneira muito mais didadica a forma como ele usa as variaveis soma e cont (linhas 39, 40) para servirem como uma especie de "guarda valor" pois elas guardam a soma e o contador guarda a quantidade total no fim do programa. 
# Bom prestar atenção também que na linha 42 ele usa o input num já pegando como recebedor o c do for:  num = int(input(f'Digite o {c} valor: ')) ou seja o proprio contador vai considerar como laço de repetição o numero digitado pelo input. Genial!
# No mais, somente treinando mais para desenvolver mais esse raciocinio lógico abstrato.

