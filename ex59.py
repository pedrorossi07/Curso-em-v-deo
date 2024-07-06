n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
op = 0
while op != 5:
    print("""--------------
Soma = [1]
Multiplicar = [2]
Maior = [3]
Novos números = [4]
Sair do programa = [5] 
--------------""")
    op = int(input(">>>>>>>>> Qual operação quer fazer? "))
    if op == 1:
        print(f"A soma {n1} + {n2} {n1+n2:.2f}")
    elif op == 2:
        print(f"A multiplicação {n1} X {n2} = {n1*n2:.2f}")
    elif op == 3:
        print(f"O maior entre {n1} e {n2} é {max(n1,n2)}")
    elif op == 4:
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite outro valor: "))
    elif op == 5:
        print("Finalizando...")
    else:
        print("Opção inválida, tente novamente")    