'''listanum = []
num = 0
while num != 999:
    num = int(input("Digite 999 para parar : "))
    if num != 999:
        listanum.append(num)
print(f"A soma dos valores digitados foi {sum(listanum)}")'''

c=0
soma = 0
num = 0
while num != 999:
    num = (int(input("Digite 999 para parar: ")))
    if num!=999:
        soma = soma +num
        c+=1
print(f"Voce digitou {c} numeros e a soma deles é: {soma}")