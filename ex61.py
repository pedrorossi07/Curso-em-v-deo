print("Gerador de P.A: ")
print('-=-'*10)
num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da P.A: "))
c=0
soma= num 
while c<10:
    print(f"{soma}", end='')
    print(' > 'if c<9 else '', end='')  
    soma = soma + razao
    c+=1