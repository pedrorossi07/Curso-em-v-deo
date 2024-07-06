valores = []
for c in range(1,6):
    valores.append(int(input("Digite um número: ")))
print(f"Seus valores foram : {valores}")
print(f"O maior número digitado foi {max(valores)}  e está localizado na posição {valores.index(max(valores))+1}")
print(f"O menor número digitado foi {min(valores)}  e está localizado na posição {valores.index(min(valores))+1}")