
tuple = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso','Grátis')
for palavra in tuple:
    print(f"\nNa palavra {palavra} temos as vogais ",end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal.lower(),end=' ')
    
