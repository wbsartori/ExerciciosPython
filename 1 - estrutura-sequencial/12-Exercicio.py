""" Tendo como dados de entrada a altura de uma pessoa, 
    construa um algoritmo que calcule seu peso ideal, 
    usando a seguinte fórmula: (72.7*altura) - 58 """

print('################################')
print('##### CALULAR PESO IDEAL #######')
print('################################')
print('') 

altura = float(input('Digita sua altura: '))
peso_ideal = ((72.2 * altura) - 58)
print('Seu peso ideal é {:.2f}'.format(peso_ideal))