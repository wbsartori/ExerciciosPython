#Faça um Programa que peça as 4 notas bimestrais e mostre a média
print('###############################')
print('####### MEDIA DAS NOTAS #######')
print('###############################')
print('')
nota1 = input('Nota 1: ')
nota2 = input('Nota 2: ')
nota3 = input('Nota 3: ')
nota4 = input('Nota 4: ')

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

print('A média das notas é: {:.2f}'.format(media))
