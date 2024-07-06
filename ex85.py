num = [[],[]]
valor = 0
for c in range (1,8):
    valor = (int(input(f"Digite o {c}º valor: ")))
    if valor % 2 == 0 :
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares são {num[0]}')
print(f"Os valores impares são {num[1]}")

'''pares = sorted([p for p in valores if p % 2 == 0])
print("Valores pares dentro da lista, em ordem crescente:")
print(pares)
impares = sorted([p for p in valores if p % 2 == 1])
print("Valores impares dentro da lista, em ordem crescente:")
print(impares)'''