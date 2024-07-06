'''frase = str(input("Digite seu frase: ")).strip().upper()
frase_sem_espaços = frase.replace(" ", "")
fraseinvertida = frase_sem_espaços[::-1]
if frase_sem_espaços == fraseinvertida:
    print(f"O inverso de {frase_sem_espaços} é {fraseinvertida}.")
    print("Temos um palímodromo")
else:
    print(f"O inverso de {frase_sem_espaços} é {fraseinvertida}.")
    print("Não temos um palímodromo")'''

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print("Temos um palímodromo")
else:
    print("Não temos um palimodromo")