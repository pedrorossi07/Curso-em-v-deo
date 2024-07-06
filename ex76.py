print("LISTAGEM DE PREÇOS")
print('-'*30)
tupla = ('Lápis',1.75,'Borracaha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livros',34.90)

for item in range(len(tupla)):
    if item % 2 ==0 :
        print(f'{tupla[item]:.<30}',end='')
    else:
        print(f'R${tupla[item]:>7.2f}')