#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print('###############################')
print('####### ÁREA DO QUADRADO ######')
print('###############################')
print('')

quadrado = float(input('Digite a medida do quadrado: '))
area = quadrado * quadrado
resultado = area * 2

print('O dobro da área do quadrado é {}' .format(resultado))