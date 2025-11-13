#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome (pode ser silva em qualquer lugar do nome)


# como eu fiz:

nome = 'Wed da Silva Torres'
nome2 = 'Roselia Tomas no Cruz'
nome3 = 'Joaquin Miguel Luis da Silva Pereira'
nome4 = 'Jaqueline Rodrigues de Souza'


print('Silva' in nome, nome.find('Silva'))
print('Silva' in nome2, nome2.find('Silva'))
print('Silva' in nome3, nome3.find('Silva'))
print('Silva' in nome4, nome4.find('Silva'))


# como professor demonstrou:


nome = str(input('Digite o seu ou qualquer nome completo: ')).strip()

print('SILVA' in nome.upper())

# ou

print('silva' in nome.lower())




#extra:
#lembrando que (in) não é um metodo e sim um operador