vel = float(input("Velocidade: "))
if vel > 80:
    print("Voce foi multado!! ")
    multa = (vel-80)*7
    print(f"Valor: R${multa:.2f}")
else:
    print("voce nao foi multado")