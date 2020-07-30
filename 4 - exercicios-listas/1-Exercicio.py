"""
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

"""

lista = []

for i in range(5):
    valor = int(input('Valor {} : '.format(i + 1)))    
    lista.append(valor)

print('lista = {}'.format(lista))