s = 0
cont = 0
for c in range(1,501):
    if c % 2 == 1 and c % 3 ==0:
        cont = cont + 1
        s += c
print(f"A soma de todos os {cont} é {s}")