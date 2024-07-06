import time
import random
valores = {}
count = 1
for c in range (1,5):
    dados = random.randint(1,6)
    print(f"O jogador {c} tirou {dados} no dado")
    valores[f'jogador {c}'] = dados
    time.sleep(1)
print("Ranking dos jogadores: ")
valores_ordenados = dict(sorted(valores.items(), key=lambda item:item[1],reverse=True)) #Função nova
for k,v in valores_ordenados.items():
    print(f"{count}º lugar : {k} com {v}")
    count +=1