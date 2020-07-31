"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

"""
aluno   = []
cont    = 0

for j in range(10):
    vetor   = []
    media   = 0    
    print('Aluno {}: '.format(j + 1))           

    for i in range(4):
        notas = float(input(' Nota {}: '.format(i + 1)))                                
        vetor.append(notas)
    
    media = (sum(vetor) / 4)
    aluno.append(media)

    if media >= 7:
        cont = cont + 1

print('{} Alunos obtiveram nota maior igual a sete.'.format(cont))