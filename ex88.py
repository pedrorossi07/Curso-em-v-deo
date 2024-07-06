import random
import time 
megasena = []
jogos = int(input("Quantos jogos você quer jogar? "))
print(f"-=-=-SORTEANDO {jogos} JOGOS.-=-=-")
for c in range(jogos):
    num = random.sample(range(1,61),6)
    megasena.append(num)
    print(f"JOGO {c+1}: {megasena}")
    megasena.clear()
    time.sleep(1)
print("-=-=-=-BOA SORTE!-=-=-=-")