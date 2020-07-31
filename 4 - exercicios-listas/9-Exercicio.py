"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

"""

soma    = 0
multi   = 0
lista   = []

for i in range(10):
    numero  = int(input('Digite o numero {}: '.format(i + 1 )))
    multi  =  numero * numero    
    lista.append(multi)

print('A soma dos quadrados do vetor é {}'.format(sum(lista)))