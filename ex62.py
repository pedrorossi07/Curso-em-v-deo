print("Gerador de P.A: ")
print('-=-'*10)
num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da P.A: "))
c=1
soma = num
totaltermos = 0
mais = 10
while mais !=0:
    totaltermos += mais
    while c<totaltermos:
        print(f"{soma} > ", end='') 
        soma = soma + razao
        c+=1
    print('PAUSA')
    mais = int(input("\nQuantos termos a mais voce quer? "))
print(f'Progressão finalizada com {totaltermos} termos')