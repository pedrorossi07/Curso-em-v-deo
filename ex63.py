print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n1 = int(input("Quantos termos quer sua sequencia? "))
c = 1
a,b=0,1
soma = a+b 
while c < n1:
    soma = a+b
    if a == 0:
        print(a,b,end=' ')
        c+=1
    print(soma,end=' ')
    a=b
    b=soma
    c+=1
    
    
