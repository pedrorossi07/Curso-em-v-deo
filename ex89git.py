galera = []
while True:

    #Coloca os dados do usuário na lista
    nome = (input("Nome: "))
    nota = int(input("Nota 1 :"))
    nota2 = int(input("Nota 2 :"))
    media = (nota + nota2) / 2
    
    galera.append([nome,[nota,nota2],media])


    cont = input("Quer contiunuar? [S/N]: ").strip().upper()[0]  #Pergunta ao usuario se quer continuar
    while cont not in 'SN':
        cont = input("Opção inválida.Quer contiunuar? [S/N]: ").strip().upper()[0]

    if cont in "N":
        break

#Imprime a tabela das médias
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for indice,aluno in enumerate(galera):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")


while True:
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
    if opc == 999:
        break
    if 0 <= opc < len(galera): #Checa se a opção está dentro dos usuarios cadastrados
        # galera[opc]: Acessa a sub-lista que contém os dados do aluno no índice opc. galera[opc][0] = Acessa o nome do aluno dentro dessa sub-lista
        print(f"As notas de {galera [opc][0]} são {galera[opc][1]} ") 
