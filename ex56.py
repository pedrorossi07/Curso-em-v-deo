somaidades = 0
listaidade = []
listanome = []
listasexo = []
for c in range (1,5):
    print(f"----- {c}ª PESSOA -----")
    nome = input("Nome: ").strip().capitalize()
    idade = int(input("Idade: "))
    somaidades +=  idade
    sexo = input("[M/F]: ").upper().strip()
    if sexo == 'M':
        listaidade.append(idade)
        listanome.append(nome)
        if max(listaidade) == listaidade[0]:
            nome = listanome[0]

        elif max(listaidade) == listaidade[1]:
            nome = listanome[1]

        elif max(listaidade) == listaidade[2]:
            nome = listanome[2]

        else :
            nome = listanome[3]
    if sexo == 'F' and idade<20:
        listasexo.append(c)

media = somaidades/4
print(f"A média das idades é {media}.")
print(f"O homem mais velho tem {max(listaidade)} anos e se chama {nome}")
if len(listasexo) <=1:
    print(f"Ao todo é {len(listasexo)} mulher com menos de 20 anos.")
else:
    print(f"Ao todo são {len(listasexo)} mulheres com menos de 20 anos.")
