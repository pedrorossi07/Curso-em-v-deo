'''perg = "F"
list = []
while perg not in ['N']:
    num = int(input("Digite um número: "))
    perg = str(input("Quer continuar ? [S/N] ")).strip().upper()
    list.append(num)
    if perg not in ['S','N']:
        print("Resposta invalida")
        perg = str(input("Quer continuar ? [S/N] ")).strip().upper()
    
print(f"A você digitou {len(list)} números e a média entre eles é {(sum(list))/len(list):.2f}")
print(f"O maior valor digitado foi {max(list)} e o menor foi {min(list)}")'''

resp = 'S'
soma = quanti = média = 0
while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quanti += 1
    if quanti == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input("Quer continuar [S/N]: ").upper().strip()[0]
média = soma/quanti
print(f"Voce digitou {quanti} números e a media foi  {média}.")
print(f"O maior número digitado foi  {maior} e o menor {menor}.")