#Faça um programa que mostre na tela uma contagem regressiva para o estouro de
#fogos de artifício, indo de 10 até 0, com uma pausa de 1 sec entre eles.

#Como eu fiz:

from time import sleep
print("VAI COMEÇAR A CONTAGEM REGRESSIVA PARA A GRANDE QUEIMA DE FOGOS!!!")
print('E É VOCE QUEM APERTA O BOTÃO PARA INICIAR A CONTAGERM!')
print('-=' * 15)
print('''[ 1 ] Para iniciar a contagem!
[ 2 ] Para cancelar!''')
print('-=' * 15)
usuario = int(input('Faça sua escolha: '))
if usuario == 2:
    print('A contagem foi cancelada!')
elif usuario == 1:
    c = 0
    for f in range(10, c-1, -1):
     sleep(1)
     print('Contagem: ', f)
    sleep(1)
    print('''  #+#+#+ + # + BOOM #+#+#+#+ + ## # # POOW## # #    # ## # ++# #
 #+##  ++ #+BOOM #++ ## ++#+#+ ## # ## ++# #+ +# # +# ## # # ## # ++
 ##+## ++  #+#  #  #+#  #+#+#+## #+#+BOOM# ## # # #++#BOOM # +# ## # +  +++
 #+##  BOOM++ #+ #++ ## ++#+#+ # #+#+#+ + ++#+#+## # ## ## # POOW++# ## # +
 #+##  ++ #+ #++ BOOM ## ++#+#+ # #+#+#+ +#+#+#+# #+# # ## # +# # ## ++# # #
 #+##  ++ #POOW+ #++ ## ++#+#+ #BOOM#+#+#+ + # +  #POOW+##+# # # # ## +## # #''')
print('Fim!')


#Como professor demosntrou:

from time import sleep
for cont in range(10, -1, -1):
   print(cont)
   sleep(0.5)
print('BUUM BUUM BUM POW')


#Anotação sobre a aula:
#Não teve misterio nesse primeiro desafio, ambos os códigos resolvem o
#problema, meu código está simplismente com uns frufrus a mais.