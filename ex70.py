print('-'*30)
print("VAREJO")
print('-'*30)
c=0
soma = 0
menor_preco = float('inf')
produto_mais_barato = ""
while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    soma = soma + preco
    if preco >1000:
        c+=1
    if preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if resp in 'N':
        break
print(f"O total gasto nas compras foi {soma:.2f} reais.")
print(f"O produto mais barato é o {produto_mais_barato} e custou {menor_preco:.2f} reais")
      