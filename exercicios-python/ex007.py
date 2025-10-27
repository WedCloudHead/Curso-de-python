#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

#eu fiz assim:

nota1 = int(input('digite a primeira nota '))
nota2 = int(input('digite a segunda nota '))
res1 = (nota1 * 50 / 100)
res2 = (nota2 * 50 / 100)
print('a media da nota 1 é: {}'.format(res1))
print('a media da nota 2 é: {}'.format(res2))


#como o professor demonstrou na correção:

n1 = float(input('A primeira nota do aluno: '))
n2 = float(input('A segunda nota do aluno: '))
média = (n1 + n2) / 2  # Um erro classico quando se executa a operação em que se quer saber a media entre dois valores é que na hora de montar a equação esquece-se o parenteses ficando assim: n1 + n2 / 2 e dessa forma o compilador vai seguir a ordem natural aritmetica da matematica que é resolver a divisão na frente da soma ou subtração, dessa forma a resposta daria 10.
print('A media entre {:.1f} e {:.1f} é igual a {:.1f} '.format(n1, n2, média))


#obs: em minha defesa que pensei que o enunciado pedia a media das notas n1 e n2 individualmente ou seja, se a nota n1 fosse 23.5 e a n2 12.4 o programa deveria retornar qual a media de n1 e a media de n2, mas no caso a questao pede a media entre n1 e n2. (de qualquer forma a minha resposta daria errado pois eu declarei com int quando deveria ter declarado com float)


#extra:

#na linha 17 os parametros {:.1f} seguem o mesmo intuito do exercicio anterior que significa que apos o ponto flutuante considere somente mais 1 numero.