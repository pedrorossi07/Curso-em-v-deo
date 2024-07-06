km = float(input("Quantos quilometros voce andou com o carro? "))
dias = int(input("Quantos dias voce ficou com o carro? "))
preco = (dias*60)+(km*0.15)
print(f"O valor do aluguel do carro ficou {preco:.2f}R$.")
