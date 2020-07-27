#Faça um Programa que leia três números e mostre o maior deles

print('##############################################################')
print('############### MAIOR / MENOR NUMERO ENTRE 3 #################')
print('##############################################################')
print('')

a   =   int(input('Digite o primeiro numero: '))  
b   =   int(input('Digite o primeiro segundo: '))  
c   =   int(input('Digite o primeiro terceiro: '))  

if (a > b and a > c and b > c):
    print('{} é o maior e {} é o menor.'.format(a, c))    
if (a > c and a > b and b < c):
    print('{} é o maior e {} é o menor.'.format(a, b))    
if (b > a and b > c and a < c):
    print('{} é o maior e {} é o menor.'.format(b, a))    
if (b > a and b > c and a > c):
    print('{} é o maior e {} é o menor.'.format(b, c))    
if (c > b and  c > a and a > b ):
    print('{} é o maior e {} é o menor.'.format(c, b))    
if (a < b and a < c and b < c):
    print('{} é o maior e {} é o menor.'.format(c, a))    