tuple = ()
tuplepar = ()
for c in range(1,5):
    num = int(input("Digite um número: "))
    tuple += (num,)
    if num % 2 == 0:
        tuplepar += (num,)

print(f"O valor 9 apareceu {tuple.count(9)} vezes")
if 3 in tuple:
    print(f"A primeira posição em que o 3 apareceu foi na {tuple.index(3)+1}º")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f"Os numeros pares são : {tuplepar}")