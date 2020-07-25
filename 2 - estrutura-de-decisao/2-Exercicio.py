"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

"""

print('##############################################################')
print('############## NEGATIVO OU POSITIVO  #########################')
print('##############################################################')
print('')

numero = int(input('Digite um numero inteiro: '))

if(numero < 0 ):
    print('O numéro {} é negativo.'.format(numero))
else:
    print('O numéro {} é positivo.'.format(numero))