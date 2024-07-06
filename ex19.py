import random 
a = input("PRIMEIRO ALUNO: ")
b = input("SEGUNDO ALUNO: ")
c = input("TERCEIRO ALUNO: ")
d = input("QUARTO ALUNO: ")

alunos = [a,b,c,d]
aleatorio = random.choice(alunos)
print(f"O aluno escolhido foi o {aleatorio}")