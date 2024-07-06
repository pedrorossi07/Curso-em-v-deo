num = int(input("Digite um número. "))
tot = 0
for c in range(1,num+1):
    if num % c ==0:
        print('\33[33m')
        tot += 1
    else:
        print('\33[31m')
    print(c,end=' ')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes.')
if tot == 2:
    print("Por isso ele é primo.")
else:
    print("Por isso não é primo.")