#faça um programa em python que abra e reproduza um audio de um arquivo MP3.


#como professor demonstrou:
#como o curso é antigo não deu pra executar o codigo da forma que o professor demonstrou, tive que fazer de uma forma diferente(explicação abaixo)


from pydub import AudioSegment
from pydub.playback import play 
musica = AudioSegment.from_file("ex021/call-me.mp3", format="mp3")
play(musica)






#Explicação:
#1) no terminal precisei entrar dentro da pasta do projeto dando os comandos: cd Documentos/GitHub/Curso-de-python/exercicios-python/ 

#2)ao entrar dentro da pasta do projeto precisei instalar o ambiente virtual pois o ubuntu não aceita mais os pacotes pip junto ao seu sistema raiz pois os pip podem alterar arquivos de sistema tambem entao dentro do ambiente virtual é tudo liberado

#3) dentro das pastas do projeto dei o comando no terminal: python3 -m venv .venv isso baixa o pacote de sistema virtual dentro da pasta do projeto

#4) depois rode ainda dentro da pasta do projeto: 
# source .venv/bin/activate  isso vai ativar o ambiente virtual dentro do projeto e o caminho vai ficar assim:
# (.venv) wed_cloud_head@wed-PC-MASTER:~/Documentos/GitHub/Curso-de-python/exercicios-python$

#5) entao instale os programas pip: 
# pip install pydub simpleaudio  esse em especifico é apenas o simpleaudio

#6) verifique se esta instalado: 
# pip list

#7) rode o programa novamente, no meu caso: 
# python3 ex021.py


#Importante: 
# dentro do vscode no terminal tambem é preciso entrar dentro do ambiente virtual entao mostre todo o caminho:

# cd Documentos/GitHub/Curso-de-python/exercicios-python$

#ao adentrar rode: source .venv/bin/activate
# e entao rode o programa, nesse caso: python3 ex021.py

#(LEMBRANDO QUE PRA ATIVAR O AMBIENTE VIRTUAL O COMANDO É ESSE: source .venv/bin/activate )

#(PARA DESATIVAR O COMANDO É ESSE: deactivate )    