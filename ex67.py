n = 0
while True:
    n = int(input("Digite um numero: "))
    if n < 0:
        break
    print ('-'*30)
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
    print ('-'*30)
print('Programa encerrado, volte sempre!')

