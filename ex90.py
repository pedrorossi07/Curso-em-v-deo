pessoa = {}
pessoa['nome'] = input("Nome : ")
pessoa['media'] = float(input("Média : "))
print(f"Nome é igual a {pessoa['nome']}")
print(f"A média é igual a {pessoa['media']}")
if pessoa['media'] < 6:
    print("Situação é igual a : reprovado.")
else:
    print("Situação é igual a aprovado")