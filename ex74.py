import random
tupla = ()
for _ in range(5):
    numero_aleatorio = random.randint(1,10)
    tupla += (numero_aleatorio, )
print(f"Os valores sorteados foram {tupla}.")
print(f"O maior valor é {max(tupla)}")
print(f"O menor valor é {min(tupla)}")
