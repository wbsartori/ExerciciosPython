#Faça um Programa que leia três números e mostre o maior deles

print('##############################################################')
print('################# MAIOR NUMERO ENTRE 3 #######################')
print('##############################################################')
print('')

a   =   int(input('Digite o primeiro numero: '))  
b =   int(input('Digite o primeiro segundo: '))  
c =   int(input('Digite o primeiro terceiro: '))  

if ( a > b and a > c):
    print('{} é maior que {} e {}'.format(a, b, c))
if ( b > a and b > c):
    print('{} é maior que {} e {}'.format(b, a, c))
if ( c > a and c > b):
    print('{} é maior que {} e {}'.format(c, a, b))