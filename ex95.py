jogador = {}
galera = []
gol=[]

while True:
    jogador.clear()

    nome = input("Nome: ").capitalize()
    jogador['nome'] = nome
    
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    jogador['gol'] = []
    total = 0
    for c in range(partidas):  
        gols = int(input(f"Quantos gols na partida {c+1}? "))
        jogador['gol'].append(gols)
        total += gols
    jogador['total']=total
    galera.append(jogador.copy())

    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        continuar = input("ERRO! Digite somente S ou N : ").strip().upper()[0]
    if continuar == "N":
        break

print('-='*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*30)
for indice, j in enumerate(galera):
    print(f'{indice:>3} ',end='')
    for d in j.values():
        print(f'{str(d):<15}',end='')
    print()

while True:
    opc = int(input("Mostrar dados de qual jogador ? (999 para parar) "))
    if opc == 999:
        break
    if 0<=opc< len(galera):
        jogador_escolhido = galera[opc]
        print(f"LEVANTAMENTO DO JOGADOR {jogador_escolhido['nome']}: ")
        for k, v in enumerate(jogador_escolhido['gol']):
            print(f"Na partida {k+1} fez {v} gols")