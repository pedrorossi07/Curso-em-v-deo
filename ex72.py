extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = -1
    while num < 0 or num> 20:
        num =int(input("Digite um valor entre 0 e 20: "))
        if num < 0 or num>20:
            print = ("Número fora do intervalo. Tente novamente")
        print(f"O seu número é {extenso[num]}")
    cont = input("Quer continuar? [S/N] ").upper().strip()[0]
    while cont not in 'SN':
        cont = input("Opção inválida. Tente novamente: ").upper().strip()[0]
    if cont == "N":
        break
    
