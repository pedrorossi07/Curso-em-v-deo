'''print("Caixa eletônico")
print('-'*30)

# Valor a ser decomposto
valor = int(input("Qual valor voce quer sacar? "))

# Calcula o resto da divisão por cada tipo de cédula
resto50 = valor % 50
resto20 = resto50 % 20
resto10 = resto20 % 10

# Calcula a quantidade de cédulas de cada valor
cedulas50 = valor // 50
cedulas20 = resto50 // 20
cedulas10 = resto20 // 10
cedulas1 = resto10 // 1  # Como resto10 % 1 é sempre 0, cedulas1 é igual a resto10

# Imprime o resultado
if cedulas50 > 0:
    print(f"Total de {cedulas50} cédulas de 50.")
if cedulas20 > 0:
    print(f"Total de {cedulas20} cédulas de 20.")
if cedulas10 > 0:
    print(f"Total de {cedulas10} cédulas de 10.")
if cedulas1 > 0:
    print(f"Total de {cedulas1} cédulas de 1.")'''

print("Caixa eletônico")
print('-'*30)
valor = int(input("Qual valor voce quer sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total>=ced:
        totced +=1
        total -= ced
    else:
        if totced>0:
            print(f"Total de {totced} cédulas de R${ced}.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
