#importando da biblioteca python.ogr o modulo random:

import random
num = random.random()
print(num)
#o random nada mais é que o computador te gerando um numero aleatorio/randomico que ele escolhe dentre 0s e 1s


import random
num = random.randint(1, 10)
print(num)
#dessa forma nota-se que random.random() mudou para random.randint() e dentro de () pode se escolher numeros que voce quer que o computador gere de forma aleatoria numeros dentro desse (), por exemplo: random.randint(2, 9) o computador ira gerar numeros aletorios sempre de 2 a 9.


import emoji
print(emoji.emojize("Olá, amigo :earth_americas:", use_aliases=True))
#aqui nessa declaração é uma forma de mostrar como importar um modulo que não vem por padrao na biblioteca python, caso queira retornar e aprender mais sobre como fazer isso, basta analizar esse trecho da explicação:
# https://youtu.be/oOUyhGNib2Q?si=5cwmPOhK-PDlgibl&t=1294