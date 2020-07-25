"""
Faça um Programa que peça dois números e imprima o maior deles.

"""

print('##############################################################')
print('####################### QUAL É MAIOR #########################')
print('##############################################################')
print('')

numero_um   = int(input('Digite um numero: '))
numero_dois = int(input('Digite mais um numero: '))

if(numero_um > numero_dois):
    print('O numero {} é maior que o numero {}. '.format(numero_um, numero_dois))
elif(numero_dois > numero_um):
    print('O numero {} é maior que o numero {}. '.format(numero_dois, numero_um))
else:
    print('São iguais.')
