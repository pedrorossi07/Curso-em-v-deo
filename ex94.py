'''cadastro = {}
nomes = []
idades = []
sexos= []
contador = 1
media = 0
soma = 0
mulher = []
acima=[]
while True:
    nome = input("Nome: ")
    nomes.append(nome)
    cadastro['nome'] = nomes

    sexo = input("Sexo [M/F]: ").strip().upper()[0]
    if sexo not in "MF":
        sexo = input("ERRO! Responda apenas com M ou F:  ").strip().upper()[0]
    sexos.append(sexo)
    cadastro['sexo'] = sexos
    if sexo == 'F':
        mulher.append(nome)

    idade = int(input("Idade : "))
    soma  += idade
    idades.append(idade)
    cadastro['idade'] = idades

    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    while continuar not in 'SN':
        continuar = input("ERRO! Responda apenas com [S/N]").strip().upper()[0]
    if continuar == 'S':
        contador += 1
    if continuar == 'N':
        break

media = soma / len(idades) #calculo da media de idades

# Identificar pessoas com idade acima da média
for i in range(len(nomes)):
    if idades[i] > media:
        acima.append({'nome': nomes[i], 'idade': idades[i]})


print(f"A)  No total foram cadastras {contador} pessoas.")
print(f"B)  A média das idades é igual {media}")
print(f"C)  As mulheres cadastradas foram : {mulher}")
print(f"D)  Lista de pessoas acima da média: ")
for k in acima:
    print(f"    Nome = {k['nome']}; idade = {k['idade']}")'''

pessoa ={}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    nome = input("Nome: ")
    pessoa['nome'] = nome

    sexo = input("Sexo [M/F]: ").strip().upper()[0]
    if sexo not in "MF":
        sexo = input("ERRO! Responda apenas com M ou F:  ").strip().upper()[0]
    pessoa['sexo'] = sexo


    idade = int(input("Idade : "))
    soma += idade
    pessoa['idade'] = idade
    
    galera.append(pessoa.copy())
    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    while continuar not in 'SN':
        continuar = input("ERRO! Responda apenas com [S/N]").strip().upper()[0]
    if continuar == 'N':
        break
    
media = soma / len(galera)

print('-='*30)
print(f"A)  Ao todo temos {len(galera)} pessoas cadastradas")
print(f"B)  A média de idades é de {media:.2f} anos.")
print("C)   As mulheres cadastradas foram : ", end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'],end=' ')
print()

print("Lista de pessoas acima da média: ")
for p in galera:
    if p['idade'] > media:
        print('     ')
        for k, v in p.items():
            print(f"{k} = {v}; ",end='')
        print()
print('<< ENCERRADO >>')