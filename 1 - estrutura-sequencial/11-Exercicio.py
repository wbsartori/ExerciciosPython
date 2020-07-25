""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. """

print('################################')
print('## CALCULAR QUESTOES A B E C  ##')
print('################################')
print('') 

print('A) o produto do dobro do primeiro com metade do segundo .')
print('B) a soma do triplo do primeiro com o terceiro.')
print('C) o terceiro elevado ao cubo.')

num_inteiro         = int(input('Digite um numero inteiro: '))
num_real            = float(input('Digite um numero de ponto flutuante: '))
num_real_dois       = float(input('Digite outro numero de ponto flutuante: '))
print('')

#Pergunta A
produto = (num_inteiro * num_inteiro)
metade_segundo = (num_real / 2)
resposta_a = produto + metade_segundo

#Pergunta B
triplo_primeiro = (num_inteiro * 3)
resposta_b = triplo_primeiro + num_real_dois

#Pergunta C
resposta_c = (num_real_dois ** 3)

print('O produto do primeiro é ({}) e a metade do segundo é ({:.2f}) desta forma o resultado é  ({:.2f}) '.format(produto, metade_segundo, resposta_a))
print('O Triplo do primeiro é ({}) e o valor do terceiro é ({:.2f}) desta forma a soma dos valores é ({:.2f})' .format(triplo_primeiro, num_real_dois, resposta_b))
print('O Terceiro valor é ({:.2f}) e seu resultado elevado ao cubo é ({:.2f})'.format(num_real_dois,resposta_c))