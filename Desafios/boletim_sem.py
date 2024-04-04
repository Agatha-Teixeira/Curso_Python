n1 = int(input('Digite a 1° nota: '))
n2 = int(input('Digite a 2° nota: '))
n3 = int(input('Digite a 3° nota: '))
n4 = int(input('Digite a 4° nota: '))


med = (n1 + n2 + n3 + n4)/4

if med >= 6:
    print ('Aluno Aprovado')

else:
    print ('Aluno Reprovado')