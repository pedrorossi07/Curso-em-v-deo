expressao = []
exp = input("Digite uma expressão matemática com parênteses: ")
expressao.append(exp)

for expr in expressao:
    print(f"A expressão {expr}",end=' ')
    if expr.count('(') == expr.count(')') and exp[0]!=')':
        print("é uma operação válida")
    else:
        print("é uma operação inválida.")