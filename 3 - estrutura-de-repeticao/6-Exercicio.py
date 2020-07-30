"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.

"""

numero = 20
i = 0
while(i < numero):
    i+= 1
    print( '{}'.format(i))     

j = 0
for j in range(numero):
    j += 1
    print( '{}'.format(j), end="")        