"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos.

"""

v_idade     = []
v_altura    = []
vetor       = []
media       = 0
cont        = 0

for i in range(5):

    print('Pessoa {}: '.format(i + 1))
    idade  = int(input('Idade: '))
    altura = float(input('Altura: '))
    v_idade.append(idade)    
    v_altura.append(altura)    

    if idade > 13:
        vetor.append(altura)        

soma = sum(v_altura)
media = (soma / 5)

for j in vetor:
    if j < media:
        cont += 1

print('-------------------------------')
print('A média de altura é de {:.2f}'.format(media))
print('{} alunos estão abaixo da média de altura.'.format(cont))