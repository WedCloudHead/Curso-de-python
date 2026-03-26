#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
#só que agora utilizando um laço for.

#Como eu fiz (17/12/2025):

num = int(input('digite um numero para ver sua tabuada: '))
print(f'A tabuada de {num} é: ')
for c in range(1, 11, 1):
    print({num}, 'X', {c}, '=', num * c)
print('Fim')
div = int(input('digite um numero para ver sua tabuada de divisão: '))
for c in range(1, 11, 1):
    print({c}, '/', {div}, '=', c / div)
print('Fim!')   

#Após voltar treinando e praticando esse foi meu segundo modo de refazer o desafio (03/03/2026):


tabu = input('Escolha uma tabuada qualquer: ').strip()
if not tabu:
    print('Você não digitou valor algum!')
else:
    try:
        tabus = int(tabu)
        if tabus < 0:
            print('A tabuada precisa ser de numeros positivos!')
        else:
             for c in range(1, 11, 1):
                 print(f'{tabus} X {c} = ', c * tabus)
             print('Fim da contagem')
    except ValueError:
        print('Digite apenas valores numericos!')
print('Fim do programa!')

#Ao fim da resolução do professor virar a explicação desse meu novo método que usei para refazer o exercicio.


#Como o professor demonstrou:

num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c:2} = {num * c}')
print('Fim da tabuada.')



# Sobre a minha primeira resolução:
# Eu nem sei ao certo qual foi a trilha de pensamento lógico que eu tive quando estava desenvolvendo o primeiro programa, foi a 4 meses atrás, aparentemente ele resolve o problema sem falhas.
# mas ainda sim está um codigo muito poluido, as informações e variaveis todas meio sem finalidade sintatica.

# Sobre a segunda resolução do problema:
# Basicamente eu adicionei um "anti-furo" no codigo que é o que o programa deve fazer caso o usuario que esteja digitando o input na hora digite algo que não é esperado, como uma letra no lugar de numero ou um input vazio.
# Basicamente isso é resolvido nas linhas 20, 21, 22, 23, 24, 25, 26, 27, 31 e 32. todas essas linhas não finalidade objetiva nenhuma com o resultado pedido pelo problema, elas apenas impedem de o programa quebrar caso o input saia de forma inesperada.

# Sobre a resolução do professor:
# As três resoluções resolvem o problema de fato, porem a minha segunda resolução tem muito mais a ver com uma estrutura lógica de fato e muito mais parecida com a resolução do professor do que a primeira.
# Na verdade a minha segunda resolução e a do professor são praticamente identicas, tirando os meus "anti-furo".
