import math
oposto = float(input("Qual é o cateto oposto do triangulo? "))
ajacente = float(input("Qual é o cateto adjacente do triangulo? "))
hip = math.hypot(oposto, ajacente)
print(f"A hipotenuza é {math.trunc(hip)}.")