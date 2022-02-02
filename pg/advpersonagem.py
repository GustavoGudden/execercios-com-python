print('Ola jogador nesse jogo vc deve acertar o personagem')

from cmath import pi
import random 

words = ['zelda', 'pikachu', 'naruto', 'goku'] 


persb = random.choice(words)

if persb == 'zelda':
    print('1º dica: the legend of ????')
    print('2ºdica: jogo da nintendo')
    print('3º dica é o nome de uma princesa')


if persb == 'pikachu':
     print('é um pokemon')
     print('seu treinador é o ash')
     print('da choque')

if persb =='goku':
    print('saia jens ??')
    print('oi eu sou o ??')
    print('vc nao vale nada ! (tapa)')


resposta = input('qual o personagem vc acha que é ???')

if resposta == persb:
    print('parabens vc acertou!!')
else:
    print('lamento vc errou')