""" Faça um Programa que peça a temperatura em graus Farenheit, 
    transforme e mostre a temperatura em graus Celsius. 
    FORMULA -> C = 5 * ((F-32) / 9). """

print('################################')
print('CONVERTER FARENHEIT PARA CELSIUS')
print('################################')
print('')    

Farenheit = float(input('Qual a temparatura em graus Farenheit: '))
Celsius = 5 * ((Farenheit - 32) / 9)
print(' A temperatura de {:.2f} graus Farenheit equivale à {:.2f} graus Celsius .'.format(Farenheit, Celsius))