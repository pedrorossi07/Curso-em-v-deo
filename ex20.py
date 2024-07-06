import random 
a = input("PRIMEIRO ALUNO: ")
b = input("SEGUNDO ALUNO: ")
c = input("TERCEIRO ALUNO: ")
d = input("QUARTO ALUNO: ")

alunos = [a,b,c,d]
random.shuffle(alunos)
print(f"A ordem de apresentação foi {alunos}")