#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5:   Abaixo do peso

# Entre 18.5 e 25:  Peso ideal 

# 25 a 30:          Sobrepeso

# 30 até 40:        Obesidade

# Acima de 40:      Obesidade morbida 

#Como eu fiz:

peso = float(input('Digite seu peso, por favor!? '))
altura = float(input('Digite sua altura, por favor!? '))
imc = peso / (altura * altura)


if imc < 18.5:
    print(f'Você não está dentro de um peso ideal em relação a sua altura, seu IMC é de {imc:.2f} Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'Você está dentro de um peso ideal em relação a sua altura, seu IMC é de {imc:.2f} Você está no peso ideal!')
elif imc >= 25  and imc <= 30:
    print(f'Você não está dentro de um peso ideal em relação a sua altura, seu IMC é de {imc:.2f} Você está em sobrepeso!')
elif imc >=30 and imc <= 40:
    print(f'Você não está dentro de um peso ideal em relação a sua altura, seu IMC é de {imc:.2f} Você está em Obesidade!')
else:
    print(f'Você definitivamente não está em um peso ideal em relação a sua altura, seu IMC é de {imc:.2f} Você está em Obesidade Morbida!')

    #Como professor demonstrou:

PESO = float(input('Qual é o seu peso? (Kg) '))
ALTURA = float(input('Qual é a sua altura? (m) '))
IMC = PESO / (ALTURA ** 2)
print(f'O IMC dessa pessoa é de: {IMC}')
if IMC < 18.5:
    print('Você está abaixo dp peso normal')
elif 18.5 <= IMC < 25:
    print('Parabéns, você está na faixa de peso normal')
elif 25 <= IMC < 30:
    print('Você está em sobrepeso')
elif 30 <= IMC < 40:
    print('Você está em obesidade!')
elif IMC >= 40:
    print('Você está em obesidade mórbida, cuidado!')

#Extra:

#Não tem muito o que falar sobre a resolução dessa aula, trabalho com condições aninhadas puras e de acordo com as teorias da aula 12, sempre ressaltando da estrutura lógica do professor em que ele reduz muito uma linha de condições utilizando os métodos permitidos pelo python3.