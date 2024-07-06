cadastro = {}
cadastro['nome'] = str(input("Nome: "))
cadastro['idade']= 2024 - int(input("Ano de nascimento : "))
cadastro['carteira'] = int(input("Carteira de trabalho (0) não tem : "))
if cadastro['carteira'] != 0:
    cadastro['aposentadoria']= (int(input("Ano de contratação : ")) + 35 + cadastro['idade']) - 2024
    cadastro['salario'] = float(input("Salário : "))


print('-='*30)
for k,v in cadastro.items():
    print(f'- {k} tem o valor {v}')