import random
print('-=-'*10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print('-=-'*10)
list = [0,1,2,3,4,5]
c=0
while True:
    valor = int(input("Diga seu valor: "))
    pi = input("Par ou Ímpar [P/I]: ").upper().strip()[0]
    comp = random.choice(list)
    if pi =="P":
        if (valor + comp)%2 == 0:
            print(f"Voce jogou {valor} e o computador {comp}. Total de {valor+comp} deu PAR")
            print('-'*30)
            print("Voce venceu... Vamos novamente")
            print('-'*30)
            c+=1
        else:
            print('-'*30)
            print(f"Voce jogou {valor} e o computador {comp}. Total de {valor+comp} deu ÍMPAR")
            print('-'*30)
            break

    elif pi == "I":
        if (valor + comp)%2 == 1:
            print(f"Voce jogou {valor} e o computador {comp}. Total de {valor+comp} deu ÍMPAR")
            print('-'*30)
            print("Voce venceu... Vamos novamente")
            print('-'*30)
            c+=1
        else:
            print('-'*30)
            print(f"Voce jogou {valor} e o computador {comp}. Total de {valor+comp} deu PAR")
            print('-'*30)
            break
    else:
        print("Escolha inválida. Por favor, escolha 'P' para par ou 'I' para ímpar.")
   

print("Voce PERDEU!")
print('-=-'*10)
print(f"GAME OVER! Você venceu {c} vezes")
           