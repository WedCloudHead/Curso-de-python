#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


#Primeira resolução:

fem = ''
mas = ''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite um sexo [M/F]: ')).strip().upper()[0]
    if sexo not in ['M', 'F']:
        print('Opção inválida! tente novamente.')

if sexo == 'F':
    sexo = 'Feminino'
else:
    if sexo == 'M':
        sexo = 'Masculino'


print(f'O sexo escolhido foi {sexo}')




#Como o professor demonstrou:


sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')

