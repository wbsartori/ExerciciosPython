"""
    Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

lista = []

for i in range(4):
    nota = float(input('Nota {}:  '.format(i+1)))
    lista.append(nota)
    media = sum(lista) / 4

print('As notas são: {}'.format(lista))
print('A media das notas é: {:.2f}'.format(media))
