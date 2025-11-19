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


#treinando mais um pouco:

Nome = str(input('Digite seu nome completo\n para que possamos ver se seu nome\n tem os sobre nomes mais comuns\n no brasil: ')).strip()

print('SILVA' in Nome.upper(), 'ROCHA' in Nome.upper(), 'TEIXEIRA' in Nome.upper(), 'SANTOS' in Nome.upper())

print('silva' in Nome.lower(), 'rocha' in Nome.lower(), 'teixeira' in Nome.lower(), 'santos' in Nome.lower())



#extra:
#lembrando que (in) não é um metodo e sim um operador