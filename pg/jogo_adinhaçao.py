from random import randint

comp = randint(0,10)

print('pensei em um numero entre 0 e 10 qual numero pensei ? ')
palpites = 0 
acertou = False
while not acertou:
     jogador = int(input("seu palpite: "))
     palpites +=1
    
     if jogador == comp:
         print('acertou')
         print(palpites)
         break
     else:
        if jogador < comp:
            print("maior")
        elif jogador>comp:
         print("menos")
  

