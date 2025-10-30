# faça um programa que converta °C em °F e mostre a conversão:

c = float(input('Informe a temperatura em °C: '))
f = ((9*c)/5)+32
print('a temperatura em {}°C corresponde a {}°F! '.format(c, f))




#importante:
#como python tambem respeita ordem de precedencia da matematica o calculo para transformar °C em °F tambem poderia ser feito sem parenteses nesse caso, pois a ordem de precedencia nessa conta ja esta correta, ou seja, poderia ter sido executada assim:
# f = 9 * c / 5 + 32 
#pois de acordo com a lei matematica primeiro se resolve as multiplicaçoes e divisoes e depois as somas e subtraçoes.