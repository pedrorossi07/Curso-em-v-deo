import random
print("Vou pensar em um número entre 0-5...")
print('-=-'*20)
num = int(input("Que número eu pensei?: "))
list =[0,1,2,3,4,5]
n=random.choice(list)
if num != n:
    print("O computador ganhou.")
else:
    print("Parabens, voce ganhou.")

