""" Faça um Programa para uma loja de tintas. 
    O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga 
    e sempre arredonde os valores para cima, isto é, considere latas cheias. """

print('################################')
print('####### CALCULAR  TINTA  #######')
print('################################')
print('') 

area            = float(input('Tamanho da área a ser pintada: '))
total_litros    = (area / 6)
total_latas     = (total_litros / 18)
total_galoes    = (total_litros / 3.6)

if (total_litros > 3.6 and total_litros <= 18):        
    print('Será necessário 1 Lata de 18 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(area, total_litros))
    print('A quantidade minima para compra é uma lata de 18 Litros no valor de R$ 80,00 reais.')

elif (total_litros <= 3.6):
    print('Será necessário 1 galão de 3.6 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(area, total_litros))
    print('A quantidade minima para compra é 1 galão de 3.6 Litros no valor de R$ 25,00 reais.')

elif (total_litros > 18 and total_latas % 2 != 0 or total_galoes % 2 != 0):
    #Resto da divisao qubrada
    resto               = total_latas % 2
    resto_galoes        = total_galoes % 2
    #Calculo do valor
    resultado           = ((total_latas - resto)  + 1) * 80
    resultado_galoes    =  ((total_galoes - resto_galoes) + 1) * 25
    #total de latas
    total_lat           = (total_latas - resto) + 1
    total_gal           = (total_galoes - resto_galoes) + 1

    print('Será necessário {:.2f} Latas de 18 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(total_lat, area, total_litros))
    print('Você precisará de {:.2f} latas de 18 litros no total o custo sairá R$ {:.2f} reais.'.format(total_lat,resultado))
    print('')
    print('###################################################################################################################')
    print('###################              Você também pode comprar em GALÕES DE 3.6 LTS.                ####################')
    print('###################################################################################################################')
    print('')
    print('Será necessário {:.2f} galões de 3.6 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(total_gal, area, total_litros))
    print('Você precisará de {:.2f} galões de 3.6 litros no total o custo sairá R$ {:.2f} reais.'.format(total_gal,resultado_galoes))
        
else:
    resultado        = total_latas * 80
    resultado_galoes = total_galoes * 25
    print('Será necessário {:.2f} Latas de 18 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(total_lat, area, total_litros))
    print('Você precisará de {:.2f} latas de 18 litros no total o custo sairá R$ {:.2f} reais.'.format(total_lat,resultado))
    print('')
    print('###################################################################################################################')
    print('###################              Você também pode comprar em GALÕES DE 3.6 LTS.                ####################')
    print('###################################################################################################################')
    print('')
    print('Será necessário {:.2f} galões de 3.6 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(total_gal, area, total_litros))
    print('Você precisará de {:.2f} galões de 3.6 litros no total o custo sairá R$ {:.2f} reais.'.format(total_gal,resultado_galoes))