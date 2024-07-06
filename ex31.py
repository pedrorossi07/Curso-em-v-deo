dist = float(input("Qual a distância da viagem em km? "))
if dist <= 200:
    preco = dist*0.5
    print(f"O valor da passagem é {preco:.2f}reais.")
else:
    preco = dist*0.45
    print(f'O valor da passagem é {preco:.2f}reais.')