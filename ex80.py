valores = []
for c in range (0,5):
    num = int(input("Digite um número: "))
    if len(valores) == 0 or num > valores[-1]:
        valores.append(num)
        print("Adicionado no final da lista...")
    else:
        pos = 0
        while pos <len(valores) and valores[pos] < num :
            pos += 1
        valores.insert(pos,num)
print(valores)
