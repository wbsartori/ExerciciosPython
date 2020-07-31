"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

"""
soma    = 0
multi   = 1
lista   = []

for i in range(5):
    numero  = int(input('Digite o numero {}: '.format(i + 1 )))
    soma    = soma + numero
    multi  *=  numero    
    lista.append(numero)

print('A soma dos números é {}'.format(soma))
print('A multiplicação dos numeros é {}'.format(multi))
print('Os numeros são -> {}'.format(lista))