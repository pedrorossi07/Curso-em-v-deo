lista_pesos = []
for c in range(1,6):
    peso = float(input(f"Qual o peso da {c}ª pessoa?"))
    lista_pesos.append(peso)
print(f"O maior peso é {max(lista_pesos)}")
print(f"O menor peso é {min(lista_pesos)}")
