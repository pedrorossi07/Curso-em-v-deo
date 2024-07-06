import math
ang = float(input("Digite um ângulo qualquer: "))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f"O conseno de {ang} é {cos:.2f}, o seno é {sen:.2f} e a tangente é {tg:.2f}.")