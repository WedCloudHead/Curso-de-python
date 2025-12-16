#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# -Média abaixo de 5.0: Reprovado
# -Média entre 5.0 e 6.9: Recuperação
# -Média de 7.0 ou superior: Aprovado

#como eu fiz:

nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))

soma = nota01 + nota02
média_reprovado = float(5.0)
média_recuperação = float(6.9)
média_aprovado = float(7.0)

if nota01 + nota02 < média_reprovado:
    print(f'Sua nota é {soma}')
    print(f'Você não atingiu a média necessaria para recuperação que é {média_reprovado}, você esta reprovado!')
elif nota01 + nota02 >= média_aprovado:
    print(f'Sua nota é {soma}')
    print(f'Você atigingiu e superou a média necessaria para a aprovação que é {média_aprovado}, você está aprovado!')
else:
    print(f'Sua nota é {soma}')
    print(f'Você está na média que é a baixo de {média_recuperação} e igual ou acima de {média_reprovado} e tem direito a fazer a recuperação!')

#Erro clássico que eu cometi, pois eu confudi o pedido do enunciado que é a média como resultado final entre as duas notas, eu simplismente peguei o resultado final somado entre as duas notas e as comparei com as médias pedidas, erro tão clássico quanto esse exercicio, abaixo a forma de como deveria ter sido feito:

nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))

soma = (nota01 + nota02) / 2
média_reprovado = float(5.0)
média_recuperação = float(6.9)
média_aprovado = float(7.0)

if soma < média_reprovado:
    print(f'Sua nota é {soma}')
    print(f'Você não atingiu a média necessaria para recuperação que é {média_reprovado}, você esta reprovado!')
elif soma >= média_aprovado:
    print(f'Sua nota é {soma}')
    print(f'Você atingiu ou superou a média necessaria para a aprovação que é {média_aprovado}, você está aprovado!')
else:
    print(f'Sua nota é {soma}')
    print(f'Você está na média que é a baixo de {média_recuperação} e igual ou acima de {média_reprovado} e tem direito a fazer a recuperação!')

#Como professor demonstrou:

nota01 = float(input('Primeira nota: '))
nota02 = float(input('Segunda nota: '))
média = (nota01 + nota02) / 2
print(f'Tirando {nota01:.1f} e {nota02:.1f}, a média do aluno é {média:.1f}')
if 7 > média >= 5:
    print('O aluno esta em RECUPERÇÃO')
elif média < 5:
    print('O aluno está REPROVADO')
elif média >= 7:
    print('O aluno está APROVADO')


#Anotações sobre esse problema:

#Após a correção ambos os códigos passaram a resolver o problema, porém, é importante notar o quão mais enxugado e direto o código demosntrado pelo professor ficou. Enquanto no meu método eu criei as variáveis medias e depois as apontei nas condições, o professor simplismente criou a variável média e depois já acrescentou as médias diretamente.
