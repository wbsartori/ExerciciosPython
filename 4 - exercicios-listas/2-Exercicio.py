"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

"""

lista = []

for i in range(10):
    valor = int(input('Valor {} : '.format(i + 1)))    
    lista.append(valor)
    

print('lista = {}'.format(sorted(lista, reverse=True)))