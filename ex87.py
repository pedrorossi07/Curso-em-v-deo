matriz = [[], [], []]
somapar = somacolun =linha = coluna = maior = 0
for contador in range(9):
    num = int(input(f"Digite um número [{linha}, {coluna}]: "))
    matriz[linha].append(num)
    coluna += 1
    if num % 2 == 0:
        somapar += num

    if coluna == 3:
        somacolun += num
        coluna = 0
        linha += 1

    for num in matriz[1]:
        if num > maior:
            maior = num

print('-=' * 30)
print('Sua matriz é:')
for linha in matriz:
    print(linha)
print('-='*30)
print(f"A soma dos valores pares é {somapar}")
print(f"A soma dos valores da terceira coluna é {somacolun}")
print(f"O maior número da 2 linha é {maior}.")