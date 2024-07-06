'''MEU SAFE
matriz = [[],[],[]]
linha = 0
coluna = 0
for contador in range (9):
    if linha == 0:
        num = int(input(f"Digite um número [{linha}, {coluna}]"))
        matriz[linha].append(num)
        coluna +=1
        if coluna ==3:
            coluna = 0
            linha +=1
    elif linha == 1:
        num = int(input(f"Digite um número [{linha}, {coluna}]"))
        matriz[linha].append(num)
        coluna +=1
        if coluna ==3:
            coluna = 0
            linha +=1
    elif linha == 2:
        num = int(input(f"Digite um número [{linha}, {coluna}]"))
        matriz[linha].append(num)
        coluna +=1
        if coluna ==3:
            coluna = 0
            linha +=1
    else:
        break
print('-='*30)
print('Sua matriz é: ')
print(matriz[0])
print(matriz[1])
print(matriz[2])'''

matriz = [[], [], []]
linha = 0
coluna = 0

for contador in range(9):
    num = int(input(f"Digite um número [{linha}, {coluna}]: "))
    matriz[linha].append(num)
    coluna += 1
    
    if coluna == 3:
        coluna = 0
        linha += 1

print('-=' * 30)
print('Sua matriz é:')
for linha in matriz:
    print(linha)
