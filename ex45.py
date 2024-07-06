import random
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jog = int(input("Qual é a sua jogada? "))
list =[0,1,2]
comp = random.choice(list)
print(comp)
if jog == 1 and comp == 0:
    print("Eu joguei pedra. Você ganhou, parabéns")
elif jog == 1 and comp == 1:
    print("Nós dois jogamos papel. Vamos novamente. ")
elif jog == 1 and comp == 2:
    print("Eu joguei tesoura. Ganhei!!")
elif jog == 0 and comp== 0:
    print("Nós dois jogamos pedra. Vamos novamente")
elif jog == 0 and comp == 1:
    print("Eu joguei papel. Ganhei!")
elif jog == 0 and comp == 2:
    print("Eu joguei tesoura, parabens voce ganhou.")
elif jog == 2 and comp == 0:
    print("Eu ganheii, joguei pedra !")
elif jog == 2 and comp == 1:
    print("Aff, escolhi papel, voce ganhou.")
else:
    print('Escolhi tesoura tambem, vamos de novo.')