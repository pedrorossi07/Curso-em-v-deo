brasileiro = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', "Chapecoence", 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Internacional', 'Fortaleza', 'Cruzeiro', 'Corinthians', 'Red Bull Bragantino', 'Cuiabá', 'Santos', 'Bahia', 'Goiás', 'América-MG', 'Vasco da Gama', 'Coritiba')

print(f"Lista de times do brasileirão: {brasileiro}")
print('-='*20)
print(f"Os primeiros 5 colocados são : {brasileiro[0:5]}")
print('-='*20)
print(f"Os 4 últimos são: {brasileiro[-4:]}")
print('-='*20)
print(f"Os times em ordem alfabética é : {sorted(brasileiro)}")
print('-='*20)
print(f"A Chapecoence está localizada na {brasileiro.index('Chapecoence')+1}º posição")