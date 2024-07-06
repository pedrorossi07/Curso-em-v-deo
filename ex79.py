valores = []
while True:
    num = int(input("Digite um número: "))
    if num not in valores:
        valores.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado... Não vou adicionar.")
    cont=input("Quer continuar? [S/N] ").upper().strip()[0]
    while cont not in 'SN':
        cont=input("Opção inválida. Quer continuar? [S/N] ").upper().strip()[0]
    if cont == 'N':
        break
print(f"Os números digitados foram : {valores}.")