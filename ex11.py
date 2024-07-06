#2metros² de parede precisa de 1 litro de tinta
l = float(input("digite a largura da parede: "))
c= float(input("Digite o comprimento da parede: "))
area= l*c
tinta = area/2
print(f"A área da parade tem dimesão {l}x{c} com área de {area}m² \n Para pintar a parede será necessário {tinta} litros de tinta.")