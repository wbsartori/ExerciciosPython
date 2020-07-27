""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
    sabendo que a decisão é sempre pelo mais barato. """

print('##############################################################')
print('################ PRODUTO COM MENOR VALOR #####################')
print('##############################################################')
print('')

preco_produto_um    = float(input('Informe o preço do produto 1: '))
preco_produto_dois  = float(input('Informe o preço do produto 2: '))
preco_produto_tres  = float(input('Informe o preço do produto 3: '))


if ( preco_produto_um < preco_produto_dois and preco_produto_um < preco_produto_tres):
    print('O produto R$ {:.2f} tem o valor menor que os produtos R$ {:.2f} e R$ {:.2f}.'.format(preco_produto_um, preco_produto_dois, preco_produto_tres))

if ( preco_produto_dois < preco_produto_um and preco_produto_dois < preco_produto_tres):
    print('O produto R$ {:.2f} tem o valor menor que os produtos R$ {:.2f} e R$ {:.2f}.'.format(preco_produto_dois, preco_produto_um,  preco_produto_tres))

if ( preco_produto_tres < preco_produto_dois and preco_produto_tres < preco_produto_um):
    print('O produto R$ {:.2f} tem o valor menor que os produtos R$ {:.2f} e R$ {:.2f}.'.format(preco_produto_tres ,preco_produto_dois, preco_produto_um))