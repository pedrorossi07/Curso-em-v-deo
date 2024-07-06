valores = []
while True:
    num = int(input("Digite um número: "))
    valores.append(num)
    cont=(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while cont not in "SN":
        cont=(input("Opção inválida. Quer continuar? [S/N] ")).upper().strip()[0]
    if cont == 'N':
        break
print(f"Você digitou {len(valores)} números.")
valores.sort(reverse=True)
print(f"A lista de maneira inversa é : {valores}")

if valores.count(5) > 0:
    print(f"A primeira vez que o número 5 aparece aparece na lista na posição {valores.index(5)}") 
else: 
    print("O número 5 não aparece na lista.")