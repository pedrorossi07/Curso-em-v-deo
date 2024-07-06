c = m = novas = 0
while True:
    print('-'*30)
    print("CADASTRE UMA PESSOA")
    print('-'*30)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Sexo: [M/F]: ").upper().strip()
    
    
    if idade > 18:
        c += 1
    if sexo == 'M':
       m += 1
    if sexo == "F" and idade < 20:
        novas += 1
    
    cont = input("Quer continuar? [S/N] ").upper().strip()
    while cont not in ['S','N']:
        cont = input("Quer continuar? [S/N] ").upper().strip()
    
    if cont =='N' :
        break
print(f"No total existem {c} pessoas com mais de 18 anos.")
print(f"Foram cadastrados {m} homens.")
print(f"Existem {novas} mulheres com menos de 20 anos")
