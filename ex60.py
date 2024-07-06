num = int(input("Digite um número para calcular seu fatorial: "))
c=num
fatorial =1
while c>0:
    print(f"{c}",end='')
    print(' x ' if c>1 else f' = {fatorial}', end='')
    fatorial *=c
    c-=1

    