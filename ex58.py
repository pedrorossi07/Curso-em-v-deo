import random
list = [0,1,2,3,4,5,6,7,8,9,10]
comp = random.choice(list)
resp = 11
toterro = 0
print("Vou pensar em um númeor de 0 a 10, tente advinhar.")
while resp != comp:
    resp = int(input("Qual valor eu pensei? "))
    if resp != comp:   
        print("Não")
        toterro += 1
    else:
        print("Parabéns, voce acertou.")
print(f"Você precisou de {toterro} tentativas para acertar")