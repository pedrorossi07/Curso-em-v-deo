pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(input("Nome: ")) 
    dados.append(int(input("Peso: ")))
    if len(pessoas)== 0:
        maior = menor = dados[1]
    else:
        if dados[1]>maior:
            maior = dados[1]
        if dados[1]<menor:
            menor=dados[1]

    pessoas.append(dados[:])
    dados.clear()
    cont =  input("Quer continuar? [S/N]: ").upper().strip()[0]

    while cont not in 'SN':
        cont =  input("Opção inválida. Quer continuar? [S/N]: ").upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso cadastrado foi {maior} kgs.")
print(f"O menor peso foi de {menor} kgs")