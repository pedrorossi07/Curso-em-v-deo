num = int(input("Digite um número inteiro: "))
opcao = int(input("Qual será a base de conversão? \n 1 para BINÁRIO \n 2 para OCTAL \n 3 para HEXADECIMAL "))
if opcao == 1:
    print(f"O valor {num} em binário é {bin(num)}")
elif opcao == 2:
    print(f"O valor {num} em octal é {oct(num)}")
elif opcao == 3:
    print(f"O valor {num} em hexadecimal é igual {hex(num)}")
else:
    print("A opção inválida, tente novamente")