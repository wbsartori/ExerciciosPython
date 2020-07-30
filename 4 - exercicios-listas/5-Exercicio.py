"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

"""

vetor = []
par = []
impar = []

for i in range(10):  
    numero = int(input('Digite o {} valor: '.format(i+1)))
    vetor.append(numero)

    if(numero % 2 == 0):
        par.append(numero)
    if(numero % 2 != 0):
        impar.append(numero)
    
print('Vetor {}'.format(vetor))
print('Pares {}'.format(par))
print('Impares {}'.format(impar))