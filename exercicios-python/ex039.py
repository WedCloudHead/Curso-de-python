#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# -Se ele ainda vai se alistar ao serviço militar
# -Se é a hora de se alistar
# -Se já passou do tempo do alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

#como eu fiz:

nascimento = int(input('Diga quantos anos você tem: '))
falta = 18 - nascimento
sobra = nascimento - 18

if nascimento < 18:
    print(f'Você ainda irá se alistar ao exercito daqui {falta} anos!')
elif nascimento == 18:
    print('Já está na hora de alistar, pois você já tem 18 anos!')
else:
    print(f'Já passou do tempo, era pra você ter se alistado a {sobra} anos atrás')

print('Procure a junta militar mais próxima do seu município para mais informações!')


#Como professor demonstrou:

from datetime import date 

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

#Extra:

#Ambos os programas resolvem o problema, porém é importante deixar claro as diferenças entre ambos as resoluções, capricho e polimento! Meu código está muito mais "carroceiro", "arcaico", pois o usuário ao executar o programa não tera detalhadamente o ano de seu nascimento, e em qual ano ele deveria ter se alistao ou irá se alistar.
# enquanto no código feito pelo professor é possivel notar as diferenças:

#linha 27: adição do módulo da biblioteca python "from datetime impor date" com a adição desse módulo o código fica muito mais preciso em trazer informações atuais do ano em que o usuário for rodar o programa! Ele funcionara independente do tempo.

#linhas 29, 36, 38, 41 e 43 todas essas variaveis foram cruciais para trazer mais exatidão e refinamento ao código, pois comparam e trazem para o usuário todas as informações necessarias possiveis sobre o intuito do problema.

