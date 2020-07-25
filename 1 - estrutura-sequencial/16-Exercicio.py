""" Faça um programa para uma loja de tintas. 
    O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
    Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. """

print('################################')
print('####### CALCULAR  TINTA  #######')
print('################################')
print('') 

area            = float(input('Tamanho da área a ser pintada: '))
total_litros    = (area / 3)
total_latas     = (total_litros / 18)

if (total_litros <= 18):    
    print('Será necessário 1 Lata de 18 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(area, total_litros))
    print('A quantidade minima para compra é uma lata de 18 Litros no valor de R$ 80,00 reais.')

elif (total_litros > 18 and total_latas % 2 != 0):
    #Resto da divisao qubrada
    resto = total_latas % 2
    #Calculo do valor
    resultado = ((total_latas - resto)  + 1) * 80
    #total de latas
    total_lat = (total_latas - resto) + 1

    print('Será necessário {:.2f} Latas de 18 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(total_lat, area, total_litros))
    print('Você precisará de {:.2f} latas de 18 litros no total o custo sairá R$ {:.2f} reais.'.format(total_lat,resultado))
        
else:
    resultado = total_latas * 80
    print('Será necessário {:.2f} Latas de 18 litros, pois para a quantidade de {:.2f} m² é necessário {:.2f} litros de tinta.'.format(total_lat, area, total_litros))
    print('Você precisará de {:.2f} latas de 18 litros no total o custo sairá R$ {:.2f} reais.'.format(total_lat,resultado))