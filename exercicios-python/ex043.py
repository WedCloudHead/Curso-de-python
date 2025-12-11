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