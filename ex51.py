num = int(input("Digite um número: "))
r = int(input("Digite a razão da P.A: "))
decimo = num + (10-1)* r
for c in range (num,decimo,r):
    print(c,end=' -> ')
print("Fim")