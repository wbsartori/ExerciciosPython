""" Tendo como dado de entrada a altura (h) de uma pessoa, 
    construa um algoritmo que calcule seu peso ideal, 
    utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 """

print('################################')
print('## CALULAR PESO IDEAL H e M   ##')
print('################################')
print('') 

print('(M) homens e (F) mulheres')
sexo    = str(input('Digite seu sexo: '))
altura  = float(input('Digite sua altura: '))

if (sexo.upper() == 'M'):
    peso_ideal = ((72.2 * altura) - 58)
    print('Para o sexo {} e a altura {:.2f}  o peso idel é {:.2f}'.format(sexo.upper(), altura, peso_ideal))
elif (sexo.upper() == 'F'):
    peso_ideal = ((72.2 * altura) - 44.7)
    print('Para o sexo {} e a altura {:.2f}  o peso idel é {:.2f}'.format(sexo.upper(), altura, peso_ideal))
else:
    print('Sexo não encontrado.')