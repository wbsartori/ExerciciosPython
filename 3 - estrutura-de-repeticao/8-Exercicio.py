"""
    Faça um programa que leia 5 números e informe a soma e a média dos números.

"""
soma = 0
media = 0

for i in range(5):
    numero = float(input('Digite valor {}: '.format(i+1)))
    soma = soma + numero
    media = soma / 5

print('A Soma dos valores é {:.2f}' .format(soma))
print('A Média dos valores é {:.2f}'.format(media))