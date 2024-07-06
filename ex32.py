ano = int(input("Qua ano quer analisar? "))
if ano%100 == 0 and ano %400 == 0:
    print("o ano é bissexto")
else:
    print("o ano não é bissexto.")