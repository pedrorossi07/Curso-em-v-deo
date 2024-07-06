valores = []
valorpar = []
valorimpar = []
while True:
    num = int(input("Digite um número: "))
    valores.append(num)
    if num % 2 == 0:
        valorpar.append(num)
    else:
        valorimpar.append(num)

    cont = input("Quer continuar? [S/N] ").upper().strip()[0]
    while cont not in 'SN':
        cont = input("Opção inválida. Quer continuar? [S/N] ").upper().strip()[0]
    if cont == "N":
        break
print(f"A lista com todos os números é {valores}.")
print(f"A lista com todos os números pares é {valorpar}.")
print(f"A lista com todos os números ímpares é {valorimpar}.")