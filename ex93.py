jogador = {}
jogador['nome'] = input('Nome : ') 
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

gols = []
soma = 0
for c in range(partidas):
    gol = (int(input(f"Quantos gols na partida {c+1}? ")))
    gols.append(gol)
    soma = soma + gol
jogador['gols'] = gols
jogador['total'] = soma
print('-='*30)
print(jogador) #primeira parte feita
print('-='*30)

for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}.") # segunda parte
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.') #terceira parte
for i, g in enumerate(gols):
    print(f"    =>  Na partida {i+1}, fez {g} gols.")
print(f"Foi um total de {soma} gols.")
