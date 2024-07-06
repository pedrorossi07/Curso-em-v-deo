frase = str(input("Digite uma frase: ")).strip().lower()
print(f"A letra a aparece {frase.count('a')} vezes.")
print(f"A primeira letra a aparece na {frase.find('a')+1} posição")
print(f"A útlima letra a aparece na {frase.rfind('a')+1} posição.")