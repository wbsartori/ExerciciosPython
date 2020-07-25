""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
    o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
    maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
    deve pagar uma multa de R$ 4,00 por quilo excedente. 
    João precisa que você faça um programa que leia a variável peso (peso de peixes) 
    e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
    na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas """

print('################################')
print('##### CALULAR MULTA POR PESO ###')
print('################################')
print('') 

peso = float(input('Digite a quantidade em KG do peixe: '))

if (peso > 50):
    excesso = peso - 50
    multa = float(excesso) * 4
    print('O Peso é de {:.2f} KG o excesso é de {:.2f} KG e a multa por excesso será de R$ {:.2f} reais.'.format(peso, excesso, multa))
else:
    print('O Peso é de {:.2f} KG o excesso é de 0 KG e a multa por excesso será de R$ 00,00 reais.'.format(peso))
    print('Não existe multa para o peso informado.')
        