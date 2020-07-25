"""
    Faça um Programa que peça a temperatura em graus Celsius, 
    transforme e mostre em graus Farenheit.
"""
print('################################')
print('CONVERTER CELSIUS PARA FARENHEIT')
print('################################')
print('')   

Celsius = float(input('Qual a temparatura em graus Celsius: '))
Farenheit = (Celsius * 9 / 5) + 32
print(' A temperatura de {:.2f} graus Celsius equivale à {:.2f} graus Farenheit.'.format(Celsius, Farenheit))