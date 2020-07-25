"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""

print('##############################################################')
print('####################### NOTAS ALUNO ##########################')
print('##############################################################')
print('')

nota_um = float(input('Digite o valor da nota 1: '))
nota_dois = float(input('Digite o valor da nota 2: '))

media = (nota_um + nota_dois) / 2

if(media >= 7 and media < 10 ):
    print('Sua media é: {} .'.format(media))
    print('Aprovado, media maior igual a 7.')
elif(media == 10):
    print('Sua media é: {} .'.format(media))
    print('Aprovado com Distinção, media igual a 10.')
else:
    print('Sua media é: {} .'.format(media))
    print('Você foi Reprovado, pois usa média é menos do que 7.')
    