from random import randrange, seed

main_numbers = []

for numbers in range(1):
  main_numbers.append(randrange(0,7))

x  = input('qual nuemro vocé acha que que o dado vai cair?')
print(f' o numero do dado que caiu é : {main_numbers}')

if x == main_numbers:
    print('parabens vc acertou ')
else:
    print('vocé errou tente novamente!!!')





