maior = 0
menos = 0
for c in range(1,8):
    nasci = int(input(f"Em que ano a {c}ª primeira pessoa nasceu?"))
    if 2024 - nasci >= 18:
        maior = c
    else:
        menos = c-maior
print(f"Ao todo tivemos {maior} pessoas maiores de idade.")
print(f"E também tivemos {menos} menores de idade.")